import  requests
from smolagents import Tool

class GifSearchTool(Tool):
    name = "gif_search"
    description = "Searches for a GIF using the Giphy API based on a given keyword."
    
    inputs = {
        "query": {"type": "string", "description": "The search term to find a relevant GIF."}
    }
    
    output_type = "string"

    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key  # Store API key

    def forward(self, query: str) -> str:
        url = f"https://api.giphy.com/v1/gifs/search?api_key={self.api_key}&q={query}&limit=1"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["data"]:
                return data["data"][0]["url"]
            else:
                return "No GIF found."
        return f"Failed to fetch GIF. HTTP Status: {response.status_code}"
