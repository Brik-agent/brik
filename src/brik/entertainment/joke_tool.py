import  requests
from smolagents import Tool

class JokeTool(Tool):
    name = "joke_tool"
    description = "Fetches a random joke."

    inputs = {}  # No input needed

    output_type = "string"

    def forward(self) -> str:
        url = "https://official-joke-api.appspot.com/random_joke"
        
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            return f"{joke['setup']} - {joke['punchline']}"
        return "Failed to fetch a joke."
