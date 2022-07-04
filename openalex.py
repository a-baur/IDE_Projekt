import requests


def oa_request(entity, filters, per_page=100, pages=None):
    """
    Request openalex API.
    """
    params = {
        "mailto": "alexander.baur@studium.uni-hamburg.de",
        "filter": ','.join([f"{comp}:{val}" for comp, val in filters.items()]),
        "per_page": per_page,
        "cursor": "*",
    }
    results = []
    page = 1
    while True:
        resp = requests.get(f"https://api.openalex.org/{entity}", params=params).json()
        if "meta" not in resp:
            raise Exception(resp)
        if "next_cursor" not in resp["meta"]:
            break
        if pages and page > pages:
            break
        results.extend(resp["results"])
        params["cursor"] = resp["meta"]["next_cursor"]
        page += 1
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
