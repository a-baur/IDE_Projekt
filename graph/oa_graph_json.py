import logging

from openalex import oa_request
from oa_graph import OpenalexGraph


def _resource_from_uri(uri):
    if not uri:
        return ""
    return uri.split("/")[-1]


class OpenalexJsonGraph(OpenalexGraph):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def add_author(self, data: dict, add_works=False):
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
            "institution": _resource_from_uri(data["last_known_institution"]["id"]),
        }
        self.logger.info(f"adding author: {params['identifier']}")
        super().add_author(**params)

        if add_works:
            works = oa_request(
                "works", filters={"author.id": data["works_api_url"].split(":")[-1]},
                pages=1,
                per_page=10
            )
            for w in works:
                self.add_work(w)
                self.add_authorship(data, w)

    def add_authorship(self, a_data, w_data):
        params = {
            "author_id": _resource_from_uri(a_data["id"]),
            "work_id":  _resource_from_uri(w_data["id"]),
        }
        self.logger.info(f"adding authorship: {params['author_id']} - {params['work_id']}")
        super().add_authorship(**params)

    def add_institution(self, data):
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
            "country": data["geo"]["country"],
            "city": data["geo"]["city"],
            "latitude": data["geo"]["latitude"],
            "longitude": data["geo"]["longitude"],
        }
        self.logger.info(f"adding institution: {params['identifier']}")
        super().add_instituion(**params)

    def add_work(self, data):
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
            "publisher": _resource_from_uri(data["host_venue"]["id"]),
            "publish_date": data["publication_date"],
            "citations": data["cited_by_count"]
        }
        self.logger.info(f"adding work: {params['identifier']}")
        super().add_work(**params)


class ParsingError(Exception):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
