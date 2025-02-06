from smolagents import Tool
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmailTool(Tool):
    name = "send_email"
    description = "Sends an email to the specified recipient using SMTP."
    inputs = {
        "to": {"type": "string", "description": "The recipient's email address (e.g., 'recipient@example.com')"},
        "subject": {"type": "string", "description": "The subject of the email"},
        "body": {"type": "string", "description": "The body content of the email"}
    }
    output_type = "string"

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the SMTP server configuration.

        Args:
            smtp_server (str): SMTP server address (e.g., 'smtp.gmail.com')
            smtp_port (int): SMTP port (e.g., 587 for TLS or 465 for SSL)
            sender_email (str): Your email address
            sender_password (str): App password or SMTP password
        """
        super().__init__()
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def forward(self, to: str, subject: str, body: str) -> str:
        """
        Sends an email using the provided SMTP settings.
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = to
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Establish connection with the SMTP server
            if self.smtp_port == 465:
                server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            else:
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()

            # Login and send email
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)
            server.quit()

            return f"Email successfully sent to {to} with subject '{subject}'."
        
        except Exception as e:
            return f"Failed to send email: {str(e)}"

from smolagents import CodeAgent

# Initialize the Email Tool with your SMTP settings (Example for Gmail)
email_tool = SendEmailTool(
    smtp_server="smtp.gmail.com",
    smtp_port=587,  # Use 465 for SSL or 587 for TLS
    sender_email="your_email@gmail.com",
    sender_password="your_app_password"  # Use App Password for Gmail
)

# Set up your model (replace with your preferred model)
from smolagents.models import HfApiModel
model = HfApiModel()

# Create the agent with the Email Tool
agent = CodeAgent(
    tools=[email_tool],
    model=model
)

# Run the agent with an email task
agent.run("Send an email to recipient@example.com with the subject 'Hello from brik' and the message 'This is a test email sent by AI.'")
