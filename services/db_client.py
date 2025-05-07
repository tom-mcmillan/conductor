import requests

class DBClient:
    """Client for the artifact database."""

    def __init__(self, endpoint):
        self.endpoint = endpoint.rstrip("/")

    def query(self, query_params):
        """Query the database."""
        url = f"{self.endpoint}/query"
        response = requests.get(url, params=query_params)
        response.raise_for_status()
        return response.json()
