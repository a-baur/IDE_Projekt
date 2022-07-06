import logging

from rdflib import Graph

from graph.oa_request import oa_request
from oa_graph_json import OpenAlexJsonGraph


def test_add_author():
    logging.basicConfig(level=logging.INFO)

    authors = oa_request("authors", filters={"last_known_institution.id": "I159176309"}, pages=1, per_page=10)

    g = OpenAlexJsonGraph(authors_from_work=True, works_from_author=True)

    for a in authors:
        g.add_author(a)

    g.serialize("graph.ttl")


def members_by_university(g=None):
    if not g:
        g = Graph()
        g.parse("../out/graph.ttl")

    knows_query = """
        SELECT (SAMPLE(?name_i) as ?NAME) (COUNT(?id_p) as ?MEMBER_COUNT)
            WHERE {
                ?id_i a schema:Organization ;
                    schema:name ?name_i .
                ?id_p schema:member ?id_i .
            }
            GROUP BY ?name_i
            ORDER BY DESC(?MEMBER_COUNT)
            LIMIT 10
    """

    q_res = g.query(knows_query)
    for row in q_res:
        for label, res in row.asdict().items():
            print(f"{label} = {res}", end="\n")
        print()


def work_number_by_author(g=None):
    if not g:
        g = Graph()
        g.parse("../out/graph.ttl")

    knows_query = """
        SELECT (SAMPLE(?name) as ?NAME) (COUNT(?work) as ?WORK_NUMBER)
        WHERE {
            ?id a schema:Person ;
                schema:name ?name ;
                schema:author ?work .
        }
        GROUP BY ?name
        ORDER BY DESC(?WORK_NUMBER)
        LIMIT 10
    """

    q_res = g.query(knows_query)
    for row in q_res:
        print(f"{row.NAME} was involved in {row.WORK_NUMBER} works")


def co_authors_by_author(g=None):
    if not g:
        g = Graph()
        print("parsing graph")
        g.parse("../out/graph.ttl")

    query = """
        SELECT (SAMPLE(?author) as ?AUTHOR) (GROUP_CONCAT(DISTINCT ?co_author; separator=", ") as ?CO_AUTHORS)
        WHERE {
            {
                SELECT ?id_author {
                    ?id_author a schema:Person .
                } LIMIT 20
            }
            ?id_author schema:name ?author ;
                schema:author ?work .
            
            ?id_co a schema:Person ;
                schema:name ?co_author ;
                schema:author ?work .
    
            FILTER(?id_author != ?id_co)
        }
        GROUP BY ?id_author
    """

    print("starting query")
    q_res = g.query(query)
    print("results:\n")
    for row in q_res:
        for label, res in row.asdict().items():
            print(f"{label} = {res}", end="\n")
        print()


def test_query_by_loc(g=None):
    if not g:
        g.parse("../out/graph.ttl")

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

    work_number_by_author()

