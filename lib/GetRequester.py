import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the initialized URL.
        Returns the raw response body as bytes.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content   # ✅ return bytes, not string

    def load_json(self):
        """
        Sends a GET request and converts the JSON response
        into a Python list or dictionary.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
