import requests


def oa_request(entity, filters):
    """
    Request openalex API.
    """
    params = {
        "mailto": "alexander.baur@studium.uni-hamburg.de",
        "filter": ','.join([f"{comp}:{val}" for comp, val in filters.items()]),
        "per_page": 100,
        "cursor": "*",
    }
    results = []
    while True:
        resp = requests.get(f"https://api.openalex.org/{entity}", params=params).json()
        if "next_cursor" not in resp["meta"]:
            break
        results.extend(resp["results"])
        params["cursor"] = resp["meta"]["next_cursor"]
    return results


if __name__ == "__main__":
    filters = {
        "country_code": "DE",
        "display_name.search": "Hamburg",
        "type": "education",
    }
    institutions = oa_request("institutions", filters)
    for inst in institutions:
        print(inst["display_name"], inst["id"], inst["geo"], "", sep="\n")
