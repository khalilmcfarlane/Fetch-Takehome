import requests
import sys
import time
import yaml

from api_endpoint import ApiEndpoint


def main():
    """
    Handle input file.
    """
    arg_length = len(sys.argv)

    if arg_length < 2:
        print("Not enough arguments. Usage: python main.py <file_name>")
        sys.exit(1)

    elif arg_length > 2:
        print("Too many arguments. Usage: python main.py <file_name>")
        sys.exit(1)
    data = parse_yaml(sys.argv[1])
    # = requests.get
    # Maybe create endpoint class?
    # If "method not in dict", set method=GET
    # If headers not in dict, don't add; if using class rep as dict
    # If body not in, don't send in request. Body is in json format (dict) use json.loads
    # ex: data = {"id": 1001} requests.post(url, json=data)
    # print(data)
    endpoints = create_endpoints(data)
    for elem in endpoints:
        start = time.time() * 1000
        response = requests.request(elem.method, url=elem.url, headers=elem.headers, data=elem.body)
        end = time.time() * 1000
        response_time = end - start
        print(response_time)
        #print(f"Requests's response time: {response.elapsed.microseconds}")
        if is_up(response, response_time):
            elem.up_requests += 1
        elem.total_requests += 1
        time.sleep(2)
        #print(response.text)
    # Test each endpoint every 15 seconds


def create_endpoints(data):
    """
    Create list of ApiEndpoint objects and return.
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


def parse_yaml(file):
    with open(file, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        return data


def is_up(res, response_time):
    """
     If HTTP Response code is between 200-299 and response latency is less than 500 ms, return True.
     """
    if res.ok and response_time < 500:
        return True
    return False


def print_result():
    """
     Print availability percentage of all endpoints.
     Availability = 100 * (Up / Total HTTP Requests)
     """
    pass


if __name__ == "__main__":
    main()
