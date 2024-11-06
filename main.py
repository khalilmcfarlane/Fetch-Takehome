import sys
import time
from typing import List

import yaml
from requests import request, Response

from api_endpoint import ApiEndpoint, associate_endpoints_with_domain


def main():
    """
    Serves as main function to execute all operations
    """
    arg_length = len(sys.argv)

    if arg_length < 2:
        print("Not enough arguments. Usage: python main.py <file_name>")
        sys.exit(1)

    elif arg_length > 2:
        print("Too many arguments. Usage: python main.py <file_name>")
        sys.exit(1)
    data = parse_yaml(sys.argv[1])

    endpoints = create_endpoints(data)
    domain_mapping = associate_endpoints_with_domain(endpoints)
    while True:
        for domain, endpoint_list in domain_mapping.items():
            up = 0
            total = 0
            for endpoint in endpoint_list:
                start = time.time()
                response = request(endpoint.method, url=endpoint.url, headers=endpoint.headers, data=endpoint.body)
                end = time.time()
                response_time = (end - start) * 1000
                if is_up(response, response_time):
                    up += 1
                total += 1
                time.sleep(15)
            print_availability_percentage(domain, up, total)


def create_endpoints(data: List) -> List[ApiEndpoint]:
    """
    Create list of ApiEndpoint objects and return.

    :param List data: Yaml file parsed into a list
    :return: List of API endpoints
    :rtype: List[ApiEndpoint]
    """
    api_endpoint_list = []
    for link in data:
        api_endpoint = ApiEndpoint(link["url"])
        if "method" in link:
            api_endpoint.method = link["method"]
        if "headers" in link:
            api_endpoint.headers = link["headers"]
        if "body" in link:
            api_endpoint.body = link["body"]

        api_endpoint_list.append(api_endpoint)
    return api_endpoint_list


def parse_yaml(file: str) -> List:
    """
    Parse yaml file

    :param str file: YAML file
    :return: Yaml file parsed into a list
    :rtype: List
    """
    with open(file, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        return data


def is_up(res: Response, response_time: float) -> bool:
    """
     If HTTP Response code is between 200-299 and response latency is less than 500 ms, return True.

    :param Response res: API Response
    :param float response_time: Response time of API request
    :return: True or False
    :rtype: bool
     """
    if 200 <= res.status_code < 300 and response_time < 500:
        return True
    return False


def print_availability_percentage(domain: str, up: int, total: int) -> None:
    """
     Print availability percentage of all endpoints.
     Availability = 100 * (Up / Total HTTP Requests)

    :param str domain: URL of domain
    :param int up: Number of API requests that were up
    :param int total: Total API requests
    :return: None
     """
    availability_percentage = round(100 * (up / total))
    print(f"{domain} has {availability_percentage}% availability percentage")


if __name__ == "__main__":
    main()
