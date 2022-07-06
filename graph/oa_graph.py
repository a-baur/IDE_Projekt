from datetime import date
from rdflib import Graph, Literal, BNode
import rdflib.plugins.sparql.processor
from rdflib.namespace import (
    SDO,  # schema.org
    RDF,
    Namespace,
)


class OpenalexGraph(Graph):
    
    def __init__(self):
        super().__init__()
        self.OA = Namespace("https://openalex.org/")
        self.DBO = Namespace("https://dbpedia.org/resource/")
        self.GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        self.bind("oa", self.OA)
        self.bind("dbo", self.DBO)
        self.bind("geo", self.GEO)

    def add_institution(self, identifier, name):
        inst = self.OA.term(identifier)
    
        self.add((inst, RDF.type, SDO.Organization))
        self.add((inst, SDO.name, Literal(name)))
    
    def add_author(self, identifier, name, institution):
        author = self.OA.term(identifier)
        inst = self.OA.term(institution)

        self.add((author, RDF.type, SDO.Person))
        self.add((author, SDO.name, Literal(name)))
        self.add((author, SDO.member, inst))

    def add_work(self, identifier, name, publisher, publish_date, citations):
        work = self.OA.term(identifier)
        publisher = self.OA.term(publisher)
        date_published = date.fromisoformat(publish_date)

        self.add((work, RDF.type, SDO.Article))
        self.add((work, SDO.name, Literal(name)))
        self.add((work, SDO.publisher, publisher))
        self.add((work, SDO.datePublished, Literal(date_published)))

    def add_venue(self, identifier, name):
        publisher = self.OA.term(identifier)

        self.add((publisher, RDF.type, SDO.Organization))
        self.add((publisher, SDO.name, Literal(name)))

    def add_is_author(self, author_id, work_id):
        author = self.OA.term(author_id)
        work = self.OA.term(work_id)

        self.add((author, SDO.author, work))

    def add_located_at(self, identifier, country, city, latitude=None, longitude=None):
        org = self.OA.term(identifier)
        loc = BNode()
        addr = BNode()

        self.add((loc, RDF.type, SDO.Place))
        self.add((loc, SDO.address, addr))

        self.add((addr, RDF.type, SDO.PostalAddress))

        if latitude and longitude:
            self.add((addr, SDO.latitude, Literal(latitude)))
            self.add((addr, SDO.longitude, Literal(longitude)))
            self.add((addr, self.GEO.geometry, Literal(f"POINT({latitude},{longitude})")))

        self.add((addr, self.DBO.country, self.DBO.term(country)))
        self.add((addr, self.DBO.city, self.DBO.term(city)))

        self.add((org, SDO.location, loc))
