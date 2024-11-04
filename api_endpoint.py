class ApiEndpoint():
    def __init__(self, url, headers=None, method="GET", body=None, up_requests=0, total_requests=0):
        self.url = url
        self.headers = headers
        self.method = method
        self.body = body
        self.up_requests = up_requests
        self.total_requests = total_requests
