import logging

from rdflib import Graph

from openalex import oa_request
from oa_graph_json import OpenalexJsonGraph


def test_add_author():
    logging.basicConfig(level=logging.INFO)

    authors = oa_request("authors", filters={"last_known_institution.id": "I159176309"}, pages=1, per_page=10)

    g = OpenalexJsonGraph(authors_from_work=True, works_from_author=True)

    for a in authors:
        g.add_author(a)

    g.serialize("graph.ttl")


def test_query_work_number():
    g = Graph()
    g.parse("graph.ttl")

    knows_query = """
        SELECT (SAMPLE(?name) as ?NAME) (COUNT(?work) as ?WORK_NUMBER)
        WHERE {
            ?id a schema:Person ;
                schema:name ?name ;
                schema:author ?work .
        }
        GROUP BY ?name
    """

    q_res = g.query(knows_query)
    for row in q_res:
        print(f"{row.NAME} created {row.WORK_NUMBER} works")


def test_query_coauthor():
    g = Graph()
    g.parse("graph/graph.ttl")

    knows_query = """
        SELECT (COUNT(?id1) as ?cnt)
        WHERE {
            ?id1 a schema:Person .
        }  
    """

    q_res = g.query(knows_query)
    for row in q_res:
        for label, res in row.labels.items():
            print(f"{label} = {res}")


if __name__ == "__main__":
    g = OpenalexJsonGraph()
    institutes = oa_request("institutions", filters={"display_name.search": "Hamburg"}, pages=1, per_page=10)
    for i in institutes:
        g.add_institution(i)
    print(g.serialize())