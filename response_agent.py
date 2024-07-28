# response_agent.py
import random
class ResponseAgent:
    def __init__(self):
        self.chat_history = []

    def respond(self, user_input):
        # Your chatbot logic goes here
        return str(random.randint(1, 100))
