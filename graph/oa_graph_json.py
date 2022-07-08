import logging
import random

from .oa_request import oa_request
from .oa_graph import OpenAlexGraph


def _resource_from_uri(uri):
    if not uri:
        # if uri is missing, create random one
        return f"_{random.randint(0, 99999999):08}"
    return uri.split("/")[-1]


class OpenAlexJsonGraph(OpenAlexGraph):
    """
    OpenAlex Graph that can parse OpenAlex responses.

    :param works_from_author: If True, adds associated works of an
        author when adding the author.
    :param authors_from_work: If True, adds associated authors of a
        work when adding the work.
    """

    def __init__(self, works_from_author=False, authors_from_work=False):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.works_from_author = works_from_author
        self.authors_from_work = authors_from_work

    def add_author(self, data: dict, add_works=True) -> None:
        """
        Add author to graph.

        :param data: OpenAlex API response json for authors.
        :param add_works: If True, add works associated with author.
        :return: None
        """
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
        }
        if data["last_known_institution"]:
            params["institution"] = _resource_from_uri(
                data["last_known_institution"]["id"]
            )
        else:
            params["institution"] = None

        self.logger.info(f"adding author: {params['identifier']}")
        super().add_author(**params)

        if self.works_from_author and add_works:
            works = oa_request(
                "works",
                filters={"author.id": data["works_api_url"].split(":")[-1]},
                pages=1,
                per_page=10
            )
            for w in works:
                self.add_work(w, add_authors=True)
                self.add_is_author(data, w)

    def add_institution(self, data: dict, add_location=True) -> None:
        """
        Add institution to graph.

        :param data: OpenAlex API response json for institutions.
        :param add_location: If True, add location associated with institution.
        :return: None
        """
        inst_params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
        }
        super().add_institution(**inst_params)

        if add_location:
            self.add_located_at(data)
        self.logger.info(f"adding institution: {inst_params['identifier']}")

    def add_venue(self, data: dict, add_location=True) -> None:
        """
        Add venue to graph.

        :param data: OpenAlex API response json for venues.
        :param add_location: If True, add location associated with venue.
        :return: None
        """
        inst_params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
        }
        super().add_venue(**inst_params)

        if add_location:
            self.add_located_at(data)
        self.logger.info(f"added venue: {inst_params['identifier']}")

    def add_work(self, data: dict, add_authors=True) -> None:
        """
        Add work to graph.

        :param data: OpenAlex API response json for works.
        :param add_authors: If True, add authors associated with work.
        :return: None
        """
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "name": data["display_name"],
            "publisher": _resource_from_uri(data["host_venue"]["id"]),
            "publish_date": data["publication_date"],
            "citations": data["cited_by_count"]
        }
        self.logger.info(f"adding work: {params['identifier']}")
        super().add_work(**params)

        if self.authors_from_work and add_authors:
            for i, authorship in enumerate(data["authorships"]):
                author = oa_request(
                    "authors",
                    filters={"openalex_id": _resource_from_uri(authorship["author"]["id"])},
                    pages=1,
                    per_page=10
                )[0]
                self.add_author(author, add_works=False)
                self.add_is_author(data, author)
                if i > 10:
                    break

    def add_is_author(self, a_data: dict, w_data: dict) -> None:
        """
        Add authorship relation between author and work.

        :param a_data: OpenAlex API response json for authors.
        :param w_data: OpenAlex API response json for works.
        :return: None
        """
        params = {
            "author_id": _resource_from_uri(a_data["id"]),
            "work_id":  _resource_from_uri(w_data["id"]),
        }
        # self.logger.info(f"adding authorship: {params['author_id']} - {params['work_id']}")
        super().add_is_author(**params)

    def add_located_at(self, data: dict) -> None:
        """
        Add location relation between institution and address.

        :param data: OpenAlex API response for institutions.
        :return:
        """
        params = {
            "identifier": _resource_from_uri(data["id"]),
            "country": data["geo"]["country"],
            "city": data["geo"]["city"],
            "latitude": data["geo"]["latitude"],
            "longitude": data["geo"]["longitude"],
        }
        super().add_located_at(**params)


class ParsingError(Exception):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
