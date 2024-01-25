from services.base_service import BaseClient
from utils.request import APIRequest

# TODO: move out this url
BASE_URI = 'https://reqres.in'


class ApiClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.request = APIRequest()

    def send_request(self, method, endpoint, payload=None, headers=None):
        if headers is None:
            headers = self.headers
        request_methods = {
            'GET': self.request.get(url=self.base_url + endpoint, headers=headers),
            'POST': self.request.post(url=self.base_url + endpoint, payload=payload, headers=headers)
        }
        return request_methods[method]
