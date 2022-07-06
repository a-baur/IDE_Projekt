import logging

from rdflib import Graph

from openalex import oa_request
from oa_graph_json import OpenAlexJsonGraph


def test_add_author():
    logging.basicConfig(level=logging.INFO)

    authors = oa_request("authors", filters={"last_known_institution.id": "I159176309"}, pages=1, per_page=10)

    g = OpenAlexJsonGraph(authors_from_work=True, works_from_author=True)

    for a in authors:
        g.add_author(a)

    g.serialize("graph.ttl")


def test_query_work_number():
    if not g:
        g = Graph()
        g.parse("graph/graph.ttl")

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


def test_query_by_loc(g=None):
    if not g:
        g = Graph()
        # g.parse("graph/graph.ttl")

    _query = """
        SELECT ?id ?name
        WHERE {
            ?id schema:location ?city .
            SERVICE <http://dbpedia.org/sparql> {
                ?city rdfs:label ?name .
            }
        }  
    """

    query = """
        SELECT ?s
        WHERE {
          SERVICE <http://dbpedia.org/sparql> {
            ?s a ?o .
          }
        }
        LIMIT 3
    """

    q_res = g.query(query)
    for row in q_res:
        for label, res in row.asdict().items():
            print(f"{label} = {res}", end="\n")
        print()


if __name__ == "__main__":
    # g = OpenalexJsonGraph()
    # institutes = oa_request("institutions", filters={"display_name.search": "Hamburg"}, pages=1, per_page=10)
    # for i in institutes:
    #     g.add_institution(i)

    test_query_by_loc()

