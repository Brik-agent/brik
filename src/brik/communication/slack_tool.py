from smolagents import Tool
import requests
import json


class SendSlackMessageTool(Tool):
    name = "send_slack_message"
    description = "Sends a rich message to a specified Slack channel using a webhook, with support for attachments and interactive buttons."
    inputs = {
        "webhook_url": {"type": "string", "description": "The Slack webhook URL for the target channel."},
        "message": {"type": "string", "description": "The main message content to send to the Slack channel."},
        "attachments": {"type": "array", "items": {"type": "object"}, "description": "Optional list of attachment objects with keys: title, text, color.", "nullable": True},
        "buttons": {"type": "array", "items": {"type": "object"}, "description": "Optional list of button objects with keys: text, value, action_id.", "nullable": True},
        "file_url": {"type": "string", "description": "Optional URL of a file to attach.", "nullable": True}
    }

    output_type = "string"

    def forward(self, webhook_url: str, message: str, attachments=None, buttons=None, file_url=None) -> str:
        """
        Sends a rich message to a Slack channel with optional attachments and interactive buttons.

        Args:
            webhook_url (str): The Slack webhook URL of the target channel.
            message (str): The text content of the message.
            attachments (list, optional): A list of attachment dicts with keys like 'title', 'text', 'color'.
            buttons (list, optional): A list of button dicts with 'text', 'value', and 'action_id'.
            file_url (str, optional): URL of a file to be attached.

        Returns:
            str: Confirmation message or error details.
        """
        try:
            # Basic message payload
            payload = {"text": message}

            # Add attachments if provided
            if attachments:
                formatted_attachments = []
                for attachment in attachments:
                    formatted_attachments.append({
                        "title": attachment.get("title", ""),
                        "text": attachment.get("text", ""),
                        "color": attachment.get("color", "#36a64f")
                    })
                payload["attachments"] = formatted_attachments

            # Add interactive buttons if provided
            if buttons:
                payload["attachments"] = payload.get("attachments", [])
                payload["attachments"].append({
                    "text": "Choose an option:",
                    "fallback": "You are unable to choose an option",
                    "callback_id": "interactive_buttons",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": button.get("action_id", "button"),
                            "text": button.get("text", "Click"),
                            "type": "button",
                            "value": button.get("value", "default")
                        }
                        for button in buttons
                    ]
                })

            # Send the message
            response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

            if response.status_code == 200:
                return "Message successfully sent to Slack channel."

            return f"Failed to send message. HTTP Status: {response.status_code}, Response: {response.text}"

        except Exception as e:
            return f"An error occurred while sending the message: {str(e)}"

# from smolagents import CodeAgent

# # Initialize the Slack Tool
# slack_tool = SendSlackMessageTool()

# # Set up your model (replace with your preferred model)
# from smolagents.models import HfApiModel
# model = HfApiModel()

# # Create the agent with the Slack Tool
# agent = CodeAgent(
#     tools=[slack_tool],
#     model=model
# )

# # Run the agent with a rich message task
# agent.run("""
# Send a message to my Slack channel using the webhook URL 'https://hooks.slack.com/services/your_webhook_url'.
# The message should say '*Hello from brik!* Here is your update.'

# Add an attachment with title 'Important Update', text 'The deployment was successful!', and color '#FF5733'.

# Include two buttons: 
# 1. Text 'View Logs' with value 'logs' and action_id 'view_logs'
# 2. Text 'Restart' with value 'restart' and action_id 'restart_server'
# """)

__all__ = [
    "SendSlackMessageTool",
]