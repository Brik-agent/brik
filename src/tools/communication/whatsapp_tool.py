from twilio.rest import Client
from smolagents import tool, CodeAgent

@tool
def send_whatsapp_message(to: str, message: str) -> str:
    """
    Sends a WhatsApp message to a specified phone number using Twilio's API.

    Args:
        to: The recipient's phone number in **international format** (e.g., '+1234567890').
        message: The text message to send via WhatsApp.

    Returns:
        str: A confirmation message if the message was sent successfully, or an error message if the sending fails.

    Raises:
        Exception: If there's an error with the Twilio API request.
    """
    # Replace with your actual Twilio credentials
    account_sid = "XXXXX" # add your twilio account sid here
    auth_token = "XXXXX" # add your twilio auth token here
    from_number = "whatsapp:+XXXXX" # add your twilio whatsapp number here

    try:
        client = Client(account_sid, auth_token)
        to_number = f"whatsapp:{to}"

        sent_message = client.messages.create(
            body=message,
            from_=from_number,
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
agent = CodeAgent(
    tools=[
        send_whatsapp_message,
    ],
    model=model,
)
agent.run("Send a WhatsApp message to +XXXX saying 'Hello i'm chatgpt but from agentexec!!'")