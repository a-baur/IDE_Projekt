import random

from rdflib import Graph, Literal, BNode
from rdflib.namespace import (
    SDO,  # schema.org
    RDF,
    Namespace,
)


def resource_from_uri(uri, res_loc=-1):
    if not uri:
        # if uri is missing, create random one
        return f"_{random.randint(0, 99999999):08}"
    return uri.split("/")[res_loc]


class OpenAlexGraph(Graph):
    """
    RDF Graph that can handle OpenAlex entities and relations.
    """

    def __init__(self):
        super().__init__()
        self.OA = Namespace("https://openalex.org/")
        self.dbr = Namespace("https://dbpedia.org/resource/")
        self.DBP = Namespace("https://dbpedia.org/property/")
        self.GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        self.DBLP = Namespace("https://dblp.org/db/conf/")
        self.bind("oa", self.OA)
        self.bind("dbr", self.dbr)
        self.bind("dbp", self.DBP)
        self.bind("geo", self.GEO)
        self.bind("dblp", self.DBLP)

    def add_institution(self, identifier: str, name: str) -> None:
        """
        Add institution to graph.

        :param identifier: OpenAlex ID.
        :param name: Name of institution.
        :return: None
        """
        inst = self.OA.term(identifier)

        self.add((inst, RDF.type, SDO.EducationalOrganization))
        self.add((inst, SDO.name, Literal(name)))

    def add_author(self, identifier: str, name: str, institution: str) -> None:
        """
        Add author to graph.

        :param identifier: OpenAlex ID
        :param name: Name of author
        :param institution: OpenAlex ID of associated institution.
        :return: None
        """
        author = self.OA.term(identifier)
        inst = self.OA.term(institution)

        self.add((author, RDF.type, SDO.Person))
        self.add((author, SDO.name, Literal(name)))
        self.add((author, SDO.member, inst))

    def add_work(self, identifier: str, name: str, date_published) -> None:
        """
        Add work to graph.

        :param identifier: OpenAlex ID
        :param name: Name of work
        :return: None
        """
        work = self.OA.term(identifier)

        self.add((work, RDF.type, SDO.Article))
        self.add((work, SDO.name, Literal(name)))
        self.add((work, SDO.datePublished, Literal(date_published)))

    def add_venue(self, work_id, identifier: str, name: str, year: str|int, city, country, lat, lng) -> None:
        """
        Add venue to graph.

        :param identifier: OpenAlex ID.
        :param name: Name of venue
        :param year: Year of event
        :param type: Type of event
        :return: None
        """
        work = self.OA.term(work_id)
        publisher = BNode()  # self.DBLP.term(identifier)
        addr = BNode()

        self.add((publisher, RDF.type, SDO.Event))
        self.add((publisher, SDO.name, Literal(name)))
        self.add((publisher, self.DBP.year, Literal(year)))

        if city and country:
            self.add((addr, RDF.type, SDO.PostalAddress))
            self.add((addr, self.DBP.country, self.dbr.term(country)))
            self.add((addr, self.DBP.city, self.dbr.term(city)))

        if lat and lng:
            self.add((addr, SDO.latitude, Literal(lat)))
            self.add((addr, SDO.longitude, Literal(lng)))
            self.add((addr, self.GEO.geometry, Literal(f"POINT({lat},{lng})")))

        if (city and country) or (lat and lng):
            self.add((publisher, SDO.location, addr))

        self.add((work, SDO.event, publisher))

    def add_associated_with_institution(self, work_id: str, inst_id) -> None:
        """
        Add institution to work.

        :param work_id: OpenAlex ID of work.
        :param inst_id: OpenAlex ID of institution.
        :return: None
        """
        work = self.OA.term(work_id)
        inst = self.OA.term(inst_id)

        self.add((work, self.DBP.institution, inst))

    def add_citations_in_year(self, identifier: str, citations: str|int, year: str|int) -> None:
        """
        Add blank node with reference to number of citations and the year.

        :param identifier: OpenAlex ID of work.
        :param citations: Number of citations
        :param year: Year with number of citations
        :return: None
        """
        work = self.OA.term(identifier)
        cite = BNode()

        self.add((work, self.DBP.citation, cite))
        self.add((cite, self.DBP.amount, Literal(citations)))
        self.add((cite, self.DBP.year, Literal(year)))

    def add_is_author(self, author_id: str, work_id: str) -> None:
        """
        Add authorship relation between author and work.

        :param author_id: OpenAlex ID of author.
        :param work_id: OpenAlex ID of work.
        :return: None
        """
        author = self.OA.term(author_id)
        work = self.OA.term(work_id)

        self.add((author, SDO.author, work))

    def add_colleague(self,  author_id: str, co_author_id: str):
        """
        Add colleague/co-author relation between author and work.

        :param author_id: OpenAlex ID of author.
        :param co_author_id: OpenAlex ID of work.
        :return: None
        """
        author = self.OA.term(author_id)
        co_author = self.OA.term(co_author_id)

        self.add((author, SDO.colleague, co_author))

    def add_located_at(
            self,
            identifier: str,
            country: str,
            city: str,
            latitude: str = None,
            longitude: str = None,
            use_dblp = False,
    ) -> None:
        """
        Add location relation between organisation and address.

        :param identifier: OpenAlex ID of organisation.
        :param country: Country of org
        :param city: City of org
        :param latitude: Latitude of org, optional.
        :param longitude: Longitude of org, optional.
        :return: None
        """
        if use_dblp:
            org = self.DBLP.term(identifier)
        else:
            org = self.OA.term(identifier)
        addr = BNode()

        self.add((addr, RDF.type, SDO.PostalAddress))

        if latitude and longitude:
            self.add((addr, SDO.latitude, Literal(latitude)))
            self.add((addr, SDO.longitude, Literal(longitude)))
            self.add((addr, self.GEO.geometry, Literal(f"POINT({latitude},{longitude})")))

        self.add((addr, self.DBP.country, self.dbr.term(country)))
        self.add((addr, self.DBP.city, self.dbr.term(city)))

        self.add((org, SDO.location, addr))
