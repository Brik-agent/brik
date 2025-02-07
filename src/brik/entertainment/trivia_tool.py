import  requests
from smolagents import Tool

class TriviaTool(Tool):
    name = "trivia_tool"
    description = "Fetches a random trivia question."
    
    inputs = {}  # No input needed

    output_type = "object"

    def forward(self) -> dict:
        url = "https://opentdb.com/api.php?amount=1&type=multiple"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                question_data = data["results"][0]
                return {
                    "question": question_data["question"],
                    "options": question_data["incorrect_answers"] + [question_data["correct_answer"]],
                    "answer": question_data["correct_answer"]
                }
        return {"error": "Failed to fetch a trivia question."}
