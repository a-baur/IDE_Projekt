from datetime import date
from rdflib import Graph, Literal, BNode

from rdflib.namespace import (
    SDO,  # schema.org
    RDF,
    Namespace,
)


class OpenalexGraph(Graph):
    
    def __init__(self):
        super().__init__()
        self.OA = Namespace("https://openalex.org/")
        self.bind("oa", self.OA)
    
    def add_institution(self, identifier, name, country, city, latitude, longitude):
        inst = self.OA.term(identifier)
        loc = BNode()
        addr = BNode()
    
        self.add((inst, RDF.type, SDO.Organization))
        self.add((inst, SDO.name, Literal(name)))
        self.add((inst, SDO.location, loc))
    
        self.add((loc, RDF.type, SDO.Place))
        self.add((loc, SDO.latitude, Literal(latitude)))
        self.add((loc, SDO.longitude, Literal(longitude)))
        self.add((loc, SDO.address, addr))

        self.add((addr, RDF.type, SDO.PostalAddress))
        self.add((addr, SDO.addressCountry, Literal(country)))
        self.add((addr, SDO.addressLocality, Literal(city)))
    
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

    def add_authorship(self, author_id, work_id):
        author = self.OA.term(author_id)
        work = self.OA.term(work_id)

        self.add((author, SDO.author, work))

    def add_venue(self, identifier, name, country, city, latitude, longitude):
        publisher = self.OA.term(identifier)
        loc = BNode()
        addr = BNode()

        self.add((publisher, RDF.type, SDO.Organization))
        self.add((publisher, SDO.name, Literal(name)))
        self.add((publisher, SDO.location, loc))

        self.add((loc, RDF.type, SDO.Place))
        self.add((loc, SDO.latitude, Literal(latitude)))
        self.add((loc, SDO.longitude, Literal(longitude)))
        self.add((loc, SDO.address, addr))

        self.add((addr, RDF.type, SDO.PostalAddress))
        self.add((addr, SDO.addressCountry, Literal(country)))
        self.add((addr, SDO.addressLocality, Literal(city)))

