import logging

from rdflib import Graph

from openalex import oa_request
from oa_graph_json import OpenalexJsonGraph


def test_add_author():
    logging.basicConfig(level=logging.INFO)

    authors = oa_request("authors", filters={"last_known_institution.id": "I159176309"}, pages=1, per_page=10)

    g = OpenalexJsonGraph()

    for a in authors:
        g.add_author(a, add_works=True)

    g.serialize("graph.ttl")


def test_query():
    g = Graph()

    knows_query = """
    SELECT DISTINCT ?work
    WHERE {
        ?a a schema:Person ;
        ?a schema:author ?work .
    }"""

    q_res = g.query(knows_query)
    for row in q_res:
        print(f"{row.work}")


if __name__ == "__main__":
    test_query()