from smolagents import Tool
from twilio.rest import Client

class SendWhatsAppMessageTool(Tool):
    name = "send_whatsapp_message"
    description = "Sends a WhatsApp message to a specified phone number using Twilio's API."
    inputs = {
        "to": {"type": "string", "description": "The recipient's phone number in international format (e.g., '+1234567890')"},
        "message": {"type": "string", "description": "The text message to send via WhatsApp"}
    }
    output_type = "string"

    def __init__(self, account_sid, auth_token, from_number):
        super().__init__()
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = f"whatsapp:{from_number}"  # Twilio WhatsApp number

    def forward(self, to: str, message: str) -> str:
        try:
            client = Client(self.account_sid, self.auth_token)
            to_number = f"whatsapp:{to}"

            sent_message = client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )

            return f"WhatsApp message sent to {to}. SID: {sent_message.sid}"
        
        except Exception as e:
            return f"Failed to send WhatsApp message: {str(e)}"

# If you want to use the ToolCallingAgent instead, uncomment the following lines as they both will work

# agent = ToolCallingAgent(
#     tools=[
#         csend_whatsapp_message,
#     ],
#     model=model,
# )

# we now give it the tool we want to use

# Initialize the WhatsApp Tool with your Twilio credentials
whatsapp_tool = SendWhatsAppMessageTool(
    account_sid="your_twilio_account_sid",
    auth_token="your_twilio_auth_token",
    from_number="+your_twilio_whatsapp_number"
)

# # Set up your model (replace with your preferred model)
# from smolagents.models import HfApiModel
# model = HfApiModel()

# # Create the agent with the WhatsApp tool
# agent = CodeAgent(
#     tools=[whatsapp_tool],
#     model=model
# )

# # Run the agent with a WhatsApp task
# agent.run("Send a WhatsApp message to +1234567890 saying 'Hello from brik!'")

__all__ = [
    "SendWhatsAppMessageTool",
]