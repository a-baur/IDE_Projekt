from rdflib import Graph


GRAPH_PATH = "../out/graph.ttl"


def query(g, q):
    if not g:
        g = Graph()
        print("parsing graph")
        g.parse(GRAPH_PATH)

    print("starting query")
    q_res = g.query(q)
    print(f"{len(q_res)} results:\n")
    for row in q_res:
        for label, res in row.asdict().items():
            print(f"{label} = {res}", end="\n")
        print()


def construct(g, q, path):
    if not g:
        g = Graph()
        print("parsing graph")
        g.parse(GRAPH_PATH)

    print("starting constructing")
    c_res = g.query(q)
    print(f"constructed graph of length {len(c_res)}.\n")
    c_res.serialize(path)


def members_by_university(g=None):
    q = """
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
    query(g, q)


def work_number_by_author(g=None):
    q = """
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
    query(g, q)


def constr_co_author_within(path, g=None):
    q = """
        CONSTRUCT{
            ?author_id a schema:Person ; 
                schema:name ?author;
                schema:colleague ?co_author_id ;
                schema:member ?inst .
        }
        WHERE {
            ?author_id a schema:Person ;
                schema:name ?author ;
                schema:colleague ?co_author_id ;
                schema:member ?inst ;
                schema:author ?work .

            ?co_author_id schema:name ?co_author ;
                schema:member ?inst .

            ?inst schema:name ?inst_name .
        }
        """
    construct(g, q, path)

def co_authors_within(g=None):
    q = """
        SELECT (SAMPLE(?author) as ?AUTHOR) (SAMPLE(?inst_name) as ?AT_INST) (GROUP_CONCAT(DISTINCT ?co_author; separator=", ") as ?CO_AUTHORS)
        WHERE {
            ?author_id a schema:Person ;
                schema:name ?author ;
                schema:colleague ?co_author_id ;
                schema:member ?inst ;
                schema:author ?work .
  
            ?co_author_id schema:name ?co_author ;
                schema:member ?inst .
  
            ?inst schema:name ?inst_name .
            
            FILTER(?author_id != ?co_author_id)
        }
        GROUP BY ?author_id
    """
    query(g, q)


def citations_by_year(g=None):
    q = """
        SELECT ?inst_name ?year (SUM(?amount) as ?AMOUNT)
        WHERE {
            {
                SELECT ?inst_id ?inst_name {
                    ?inst_id a schema:EducationalOrganization ;
                        schema:name ?inst_name .
                }
            }
            ?work dbp:institution ?inst_id ;
                dbp:citation [
                    dbp:amount ?amount ;
                    dbp:year ?year
                ] .
        }
        GROUP BY ?inst_name ?year
        ORDER BY ?inst_name DESC(?year)
    """
    query(g, q)


def location_by_inst(g=None):
    q = """
        SELECT (SAMPLE(?city) as ?CITY) (GROUP_CONCAT(DISTINCT ?inst_name; separator=", ") as ?INST) 
        WHERE {
            ?id_inst a schema:EducationalOrganization ;
                schema:name ?inst_name ;
                schema:location [
                    dbo:city ?city
                ]
        }
        GROUP BY ?city
    """
    query(g, q)


if __name__ == "__main__":
    GRAPH_PATH = "out/graph.ttl"
    constr_co_author_within(path="out/construction.ttl")

