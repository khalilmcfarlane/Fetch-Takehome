from collections import defaultdict
from typing import DefaultDict, List
from urllib.parse import urlparse


class ApiEndpoint:
    def __init__(self, url, headers=None, method="GET", body=None, up_requests=0, total_requests=0):
        self.url = url
        self.headers = headers
        self.method = method
        self.body = body
        self.up_requests = up_requests
        self.total_requests = total_requests


def get_main_domain(url: str) -> str:
    """
    Parse domain from url.

    :param str url: URL parsed from yaml file
    :return: URL domain
    :rtype: str
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc


def associate_endpoints_with_domain(endpoints: List[ApiEndpoint]) -> DefaultDict[str, List[ApiEndpoint]]:
    """
    Return dictionary mapping domain to list of subdomains
    :param List[ApiEndpoint] endpoints: List of URL endpoints
    :return: Mapping of domain to list of subdomains
    :rtype: DefaultDict[str, List[ApiEndpoint]]
    """
    domain_mapping = defaultdict(list)

    for endpoint in endpoints:
        main_domain = get_main_domain(endpoint.url)
        domain_mapping[main_domain].append(endpoint)
    return domain_mapping
