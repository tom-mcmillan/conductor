import requests

class ArtifactingClient:
    """Client for the artifacting service."""

    def __init__(self, endpoint):
        self.endpoint = endpoint.rstrip("/")

    def create_artifact(self, data):
        """Create a new artifact."""
        url = f"{self.endpoint}/artifacts"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
