import requests

class ArgdownClient:
    """Client for the Argdown factory."""

    def __init__(self, endpoint):
        self.endpoint = endpoint.rstrip("/")

    def process(self, artifact):
        """Process an artifact."""
        url = f"{self.endpoint}/process"
        response = requests.post(url, json=artifact)
        response.raise_for_status()
        return response.json()
