import base64
import requests
from smolagents import Tool
import base64

class SpotifyTool(Tool):
    name = "spotify_search"
    description = "Searches for a song on Spotify based on the track name."
    
    inputs = {
        "track_name": {"type": "string", "description": "The name of the track to search for."}
    }
    
    output_type = "string"

    def __init__(self, client_id: str, client_secret: str):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self) -> str:
        auth_url = "https://accounts.spotify.com/api/token"
        auth_headers = {
            "Authorization": "Basic " + base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode(),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        auth_data = {"grant_type": "client_credentials"}
        
        auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
        if auth_response.status_code == 200:
            return auth_response.json().get("access_token")
        return None

    def forward(self, track_name: str) -> str:
        token = self.get_access_token()
        if not token:
            return "Failed to authenticate with Spotify."

        search_url = f"https://api.spotify.com/v1/search?q={track_name}&type=track&limit=1"
        headers = {"Authorization": f"Bearer {token}"}
        
        search_response = requests.get(search_url, headers=headers)
        if search_response.status_code == 200:
            tracks = search_response.json().get("tracks", {}).get("items", [])
            if tracks:
                return tracks[0]["external_urls"]["spotify"]
            else:
                return "No matching track found."
        return "Failed to fetch song details."
