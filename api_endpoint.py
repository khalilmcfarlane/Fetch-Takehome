from collections import defaultdict
from typing import List
from urllib.parse import urlparse


class ApiEndpoint:
    def __init__(self, url, headers=None, method="GET", body=None, up_requests=0, total_requests=0):
        self.url = url
        self.headers = headers
        self.method = method
        self.body = body
        self.up_requests = up_requests
        self.total_requests = total_requests


def get_main_domain(url):
    """
    Parse domain from url.
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc


def associate_endpoints_with_domain(endpoints: List[ApiEndpoint]):
    """
    Return dictionary mapping domain to list of subdomains
    String to List[ApiEndpoint] Mapping
    """
    domain_mapping = defaultdict(list)

    for endpoint in endpoints:
        main_domain = get_main_domain(endpoint.url)
        domain_mapping[main_domain].append(endpoint)
    return domain_mapping
