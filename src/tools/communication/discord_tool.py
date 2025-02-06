from smolagents import Tool
import requests


class SendDiscordMessageTool(Tool):
    name = "send_discord_message"
    description = "Sends a message to a specified Discord channel using a webhook."
    inputs = {
        "webhook_url": {"type": "string", "description": "The Discord webhook URL for the target channel."},
        "message": {"type": "string", "description": "The message to send to the Discord channel."}
    }
    output_type = "string"

    def forward(self, webhook_url: str, message: str) -> str:
        """
        Sends a message to a Discord channel using the provided webhook URL.

        Args:
            webhook_url (str): The webhook URL of the Discord channel.
            message (str): The content of the message to send.

        Returns:
            str: Success confirmation or error message.
        """
        try:
            data = {"content": message}
            response = requests.post(webhook_url, json=data)

            if response.status_code == 204:
                return f"Message successfully sent to Discord channel."
            else:
                return f"Failed to send message. HTTP Status: {response.status_code}, Response: {response.text}"
        
        except Exception as e:
            return f"An error occurred while sending the message: {str(e)}"

from smolagents import CodeAgent

# Initialize the Discord Tool (Webhooks don't require additional credentials)
discord_tool = SendDiscordMessageTool()

# Set up your model (replace with your preferred model)
from smolagents.models import HfApiModel
model = HfApiModel()

# Create the agent with the Discord Tool
agent = CodeAgent(
    tools=[discord_tool],
    model=model
)

# Run the agent with a Discord message task
agent.run("Send a message to my Discord channel saying 'Hello from brik!' using the webhook URL 'https://discord.com/api/webhooks/your_webhook_url'")
