"""
Predefined queries for analysis of graph.
"""
import json

import pandas as pd
from rdflib import Graph


DEFAULT_GRAPH = "../out/graph.ttl"

UNI_LABELS = {
    "haw": "Hamburg University of Applied Sciences",
    "tuhh": "Hamburg University of Technology",
    "uhh": "Universität Hamburg"
}

UNI_QUERY_LIST = (
    '"Hamburg University of Applied Sciences" '
    '"Hamburg University of Technology" '
    '"Universität Hamburg"'
)


def query(g, q, verbose=True):
    """
    Query graph.

    :param g: Graph to query.
    :param q: Query
    :param verbose: Print results.
    :return: query result
    """
    if not g:
        g = Graph()
        print("parsing graph")
        g.parse(DEFAULT_GRAPH)

    print("starting query")
    q_res = g.query(q)
    print(f"{len(q_res)} results:\n")
    if verbose:
        for row in q_res:
            for label, res in row.asdict().items():
                print(f"{label} = {res}", end="\n")
            print()
    return q_res


def construct(g, q, path):
    if not g:
        g = Graph()
        print("parsing graph")
        g.parse(DEFAULT_GRAPH)

    print("starting constructing")
    c_res = g.query(q)
    print(f"constructed graph of length {len(c_res)}.\n")
    c_res.serialize(path, format="turtle")
    return c_res


def res_to_dataframe(res):
    """
    Convert query result to dataframe.
    """
    res_json = res.serialize(format="json")
    res_dict = json.loads(res_json)["results"]["bindings"]
    res_df = pd.DataFrame.from_records(res_dict)
    res_df = res_df.applymap(lambda x: x["value"])
    res_df = res_df.apply(pd.to_numeric, errors="ignore")
    return res_df


def select_pubs_by_author(g=None):
    """
    Get the number of publication by author.
    """
    q = f"""
        SELECT
            (SAMPLE(?name) as ?NAME)
            (SAMPLE(?inst_name) as ?INSTITUTION)
            (COUNT(?work) as ?WORK_NUMBER)
        WHERE {{
            ?id a schema:Person ;
                schema:name ?name ;
                schema:author ?work ;
                schema:member [
                    schema:name ?inst_name 
                ] .
            VALUES ?inst_name {{ {UNI_QUERY_LIST} }}
        }}
        GROUP BY ?name
        ORDER BY DESC(?WORK_NUMBER)
    """
    return query(g, q)


def select_pubs_for_author(author, g=None):
    """
    Get the number of publication for specific author.
    """
    q = f"""
        SELECT
            (COUNT(?work) as ?WORK_NUMBER)
        WHERE {{
            ?id a schema:Person ;
                schema:name ?name ;
                schema:author ?work ;
            
            VALUES ?name {{ "{author}" }}
        }}
        GROUP BY ?name
        ORDER BY DESC(?WORK_NUMBER)
    """
    return query(g, q)


def select_citations_by_year(g=None):
    """
    Get number of citations for a university by year.
    """
    q = f"""
        SELECT ?inst_name ?year (SUM(?amount) as ?AMOUNT)
        WHERE {{
            {{
                SELECT ?inst_id ?inst_name {{
                    ?inst_id a schema:EducationalOrganization ;
                        schema:name ?inst_name .
                }}
            }}
            ?work dbp:institution ?inst_id ;
                dbp:citation [
                    dbp:amount ?amount ;
                    dbp:year ?year
                ] .
            
            VALUES ?inst_name {{ {UNI_QUERY_LIST} }}
        }}
        GROUP BY ?inst_name ?year
        ORDER BY ?inst_name DESC(?year)
    """
    return query(g, q)


def construct_co_author_network(inst_a: str, inst_b: str, path, g=None):
    """
    Get co-author network between institutions a and b.
    a and b can be the same institution, giving the co-
    author network within a university.

    :param inst_a: Name of institution a
    :param inst_b: Name of institution b
    :param path: Path to save constructed graph to.
    :param g: Graph to perform query on. None -> Use default Graph.
    :return: None
    """
    q = f"""
        CONSTRUCT{{
            ?author_id a schema:Person ; 
                schema:name ?author ;
                schema:colleague ?co_author_id ;
                schema:member ?inst_a_id .
            
            ?co_author_id a schema:Person ;
                schema:name ?co_author_name ;
                schema:colleague ?author_id ;
                schema:member ?inst_b_id .
        }}
        WHERE {{
            ?author_id a schema:Person ;
                schema:name ?author ;
                schema:colleague ?co_author_id ;
                schema:member ?inst_a_id ;
                schema:author ?work .

            ?co_author_id schema:name ?co_author ;
                schema:name ?co_author_name ;
                schema:member ?inst_b_id .
                
            ?inst_a_id schema:name '{inst_a}' .
            ?inst_b_id schema:name '{inst_b}' .
        }}
        """
    return construct(g, q, path)


def select_co_author_within(g=None):
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
    return query(g, q)


def select_venue_coord_by_uni(g=None):
    """
    Get list of venue coordinates by university.
    """
    q = f"""
        SELECT
            (SAMPLE(?inst_name) as ?INST)
            (CONCAT('[', GROUP_CONCAT(CONCAT('(', str(?lat), ', ', str(?lng), ')'); separator=', '), ']') as ?COORD)
            (CONCAT('[', GROUP_CONCAT(CONCAT('"', ?ven_name, '"'); separator=', '), ']') as ?VENUE)
        WHERE {{
            ?id_inst a schema:EducationalOrganization ;
                schema:name ?inst_name .
                
            VALUES ?inst_name {{ {UNI_QUERY_LIST} }}
            
            ?work dbp:institution ?id_inst ;
                schema:event [
                    schema:name ?ven_name ;
                    schema:location [
                        schema:latitude ?lat ;
                        schema:longitude ?lng
                    ]
                ]
        }}
        GROUP BY ?inst_name
    """
    return query(g, q)


def select_members_by_inst(g=None):
    q = f"""
        SELECT (SAMPLE(?inst_name) as ?INSTITUTE) (COUNT(?id_author) as ?MEMBERS)
        WHERE {{
            ?id_inst a schema:EducationalOrganization ;
                schema:name ?inst_name .
            
            VALUES ?inst_name {{ {UNI_QUERY_LIST} }}
            
            ?id_author a schema:Person ;
                schema:member ?id_inst . 
        }}
        GROUP BY ?inst_name
    """
    return query(g, q)


if __name__ == "__main__":
    DEFAULT_GRAPH = "../out/final_graph.ttl"
    res = select_venue_coord_by_uni()
    df = res_to_dataframe(res)
    print(df.head(10))
