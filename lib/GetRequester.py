import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []

        loaded_data = json.loads(self.get_response_body())
        for data in loaded_data:
            data_list.append(data)
        return data_list