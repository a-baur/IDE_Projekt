from urllib.parse import quote_plus

from graph.oa_graph_json import OpenAlexGraph, _resource_from_uri
from graph.oa_request import oa_request


SAVE_AFTER_BATCH = 50


def get_dbo_uri(term: str):
    if not term:
        return
    term = term.replace(' ', '_')
    resource = quote_plus(term)
    return "https://dbpedia.org/resource/" + resource


def get_institutions(g):
    q = """
        SELECT DISTINCT ?inst_id
        WHERE {
            ?inst_id a schema:EducationalOrganization .
            FILTER NOT EXISTS {
              ?inst_id schema:location ?x
            }
        }
    """
    q_res = g.query(q)
    result = []
    for row in q_res:
        result.append(row.inst_id)
    return result


if __name__ == "__main__":
    g = OpenAlexGraph()
    g.parse("out/graph.ttl")

    print(f"\n\nNodes: {len(g)}")
    institutions = get_institutions(g)
    print(f"adding {len(institutions)} institutions\n")
    for i, inst in enumerate(institutions):
        print(f"\rAdding location for institution, no. {i}", end="")
        inst_id = _resource_from_uri(inst)
        if inst_id.startswith("_"):
            continue
        _filter = {"openalex_id": str(inst)}
        loc = oa_request("institutions", _filter)[0]["geo"]
        dbo_country = get_dbo_uri(loc["country"])
        dbo_city = get_dbo_uri(loc["city"])
        g.add_located_at(
            identifier=inst_id,
            country=_resource_from_uri(dbo_country),
            city=_resource_from_uri(dbo_city),
            latitude=loc["latitude"],
            longitude=loc["longitude"]
        )
        if i % SAVE_AFTER_BATCH == 0:
            print(f"\nSaving for iteration {i}\n")
            g.serialize("out/loc_graph.ttl")
    g.serialize("out/loc_graph3.ttl")
    print(f"\n\nNodes: {len(g)}")
