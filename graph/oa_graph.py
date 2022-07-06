from datetime import date
from rdflib import Graph, Literal, BNode
import rdflib.plugins.sparql.processor
from rdflib.namespace import (
    SDO,  # schema.org
    RDF,
    Namespace,
)


class OpenAlexGraph(Graph):
    """
    RDF Graph that can handle OpenAlex entities and relations.
    """

    def __init__(self):
        super().__init__()
        self.OA = Namespace("https://openalex.org/")
        self.DBO = Namespace("https://dbpedia.org/resource/")
        self.DBP = Namespace("https://dbpedia.org/property/")
        self.GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        self.bind("oa", self.OA)
        self.bind("dbo", self.DBO)
        self.bind("dbp", self.DBP)
        self.bind("geo", self.GEO)

    def add_institution(self, identifier: str, name: str) -> None:
        """
        Add institution to graph.

        :param identifier: OpenAlex ID.
        :param name: Name of institution.
        :return: None
        """
        inst = self.OA.term(identifier)

        self.add((inst, RDF.type, SDO.Organization))
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

    def add_work(self, identifier: str, name: str, publisher: str, publish_date: str) -> None:
        """
        Add work to graph.

        :param identifier: OpenAlex ID
        :param name: Name of work
        :param publisher: OpenAlex ID of publishing venue
        :param publish_date: Date of publication
        :param citations: Number of citations
        :return: None
        """
        work = self.OA.term(identifier)
        if publisher:
            publisher = self.OA.term(publisher)
        date_published = date.fromisoformat(publish_date)

        self.add((work, RDF.type, SDO.Article))
        self.add((work, SDO.name, Literal(name)))
        self.add((work, SDO.publisher, publisher))
        self.add((work, SDO.datePublished, Literal(date_published)))

    def add_venue(self, identifier: str, name: str) -> None:
        """
        Add venue to graph.

        :param identifier: OpenAlex ID.
        :param name: Name of venue
        :return: None
        """
        publisher = self.OA.term(identifier)

        self.add((publisher, RDF.type, SDO.Organization))
        self.add((publisher, SDO.name, Literal(name)))

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

    def add_located_at(
            self,
            identifier: str,
            country: str,
            city: str,
            latitude: str = None,
            longitude: str = None
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
        org = self.OA.term(identifier)
        addr = BNode()

        self.add((addr, RDF.type, SDO.PostalAddress))

        if latitude and longitude:
            self.add((addr, SDO.latitude, Literal(latitude)))
            self.add((addr, SDO.longitude, Literal(longitude)))
            self.add((addr, self.GEO.geometry, Literal(f"POINT({latitude},{longitude})")))

        self.add((addr, self.DBO.country, self.DBO.term(country)))
        self.add((addr, self.DBO.city, self.DBO.term(city)))

        self.add((org, SDO.location, addr))
