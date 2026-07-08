import requests

BASE_URL = "https://internito.csesnitw.in"
API_ENDPOINT = "/api/experiences"


class InternitoAPI:
    """Client for communicating with the interNito API."""

    def __init__(self):
        self.session = requests.Session()
        self.base_url = BASE_URL

    def fetch_interviews(self):
        """Fetch all interview experiences."""

        url = self.base_url + API_ENDPOINT

        response = self.session.get(url, timeout=30)

        response.raise_for_status()

        data = response.json()

        return data
