# **brik 🧱**
from san fransisco with ❤️

**a minimal execution layer for ai agents to automate real-world tasks**

brik makes it simple for ai agents to take real-world actions—beyond just generating text. whether you’re building an agent that sends messages, books appointments, analyzes data, or manages workflows, brik provides modular tools to help you bridge the gap between "thinking" and "doing."

---

### **what is brik?**

brik is an execution framework for ai agents. think of it as a library of modular tools that agents can use to take actions in the real world.  
some examples:
- sending a whatsapp message
- booking flights or reservations
- automating email workflows
- running web searches
- integrating with productivity tools like slack or discord

it’s lightweight, developer-friendly, and built with modularity in mind.

---

### **features**

- **minimal and modular**: simple, no-frills tools that are easy to plug into your agent workflows.
- **real-world actions**: enable agents to go beyond generating text and actually execute tasks.
- **developer-first**: designed to be intuitive, with clear apis and minimal setup.
- **hugging face integrations**: works seamlessly with your favorite llms from openai, hugging face, or local models.

---

### **quickstart**

#### **install brik**

```bash
pip install brik
```

#### **example: sending a whatsapp message**

```python
from brik.tools import SendWhatsAppMessageTool

# initialize the whatsapp tool with your twilio credentials
whatsapp_tool = SendWhatsAppMessageTool(
    account_sid="your_twilio_account_sid",
    auth_token="your_twilio_auth_token",
    from_number="+your_twilio_whatsapp_number"
)

# send a message
response = whatsapp_tool.forward(to="+1234567890", message="hello from brik!")
print(response)
```

#### **example: using brik with an agent**

```python
from brik.tools import SendSlackMessageTool, SendEmailTool
from smolagents import CodeAgent
from smolagents.models import HfApiModel

# initialize tools
slack_tool = SendSlackMessageTool()
email_tool = SendEmailTool(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    sender_email="your_email@gmail.com",
    sender_password="your_app_password"
)

# initialize the agent
model = HfApiModel()
agent = CodeAgent(tools=[slack_tool, email_tool], model=model)

# run the agent
agent.run("send a slack message saying 'launch successful' and email a summary to the team.")
```

---

### **tools**

brik includes tools for common agent tasks. here are a few examples:

#### **communication**
- `send_whatsapp_message`: send whatsapp messages using twilio.
- `send_slack_message`: send messages to slack channels via webhook.
- `send_email`: automate email workflows with smtp.

#### **web automation**
- `web_scraper_tool`: scrape content from web pages.
- `search_wikipedia`: fetch summaries from wikipedia.
- `run_google_search`: perform google searches programmatically.

#### **productivity**
- `calendar_integration`: schedule events and manage tasks.
- `time_zone_converter`: convert time zones for global workflows.

#### **custom tools**
brik is extensible—create and add your own tools as needed.

---

### **installation**

install brik using pip:

```bash
pip install brik
```

---

### **roadmap**

we’re just getting started. here’s what’s coming next:

- **more tools**: integrations with calendly, notion, and trello.
- **file automation**: pdf reading, qr code generation, and more.
- **security**: sandboxed execution environments for safer automation.
- **agent playground**: a simple ui to test tools and build workflows.

---

### **contributing**

contributions are welcome! here’s how you can get involved:

1. **fork the repo**  
2. **add your tool**  
3. **open a pull request**

make sure your code passes all tests by running:

```bash
pytest
```

we’re happy to collaborate on ideas or new integrations—just open an issue to discuss.

---

### **license**

this project is licensed under the mit license. see the [LICENSE](./LICENSE) file for details.

---

### **citation**

if you use brik in your work, please consider citing it:

```
@misc{brik,
  author = {Your Name},
  title = {brik: a minimal execution layer for ai agents},
  year = {2024},
  howpublished = {\url{https://github.com/yourusername/brik}},
}
```

---

### **questions?**

feel free to open an issue or reach out directly. let’s build something amazing 🚀
