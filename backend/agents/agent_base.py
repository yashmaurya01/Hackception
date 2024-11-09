# backend/agents/agent_base.py

import openai
import os

class AgentBase:
    def __init__(self, name, role, persona):
        self.name = name
        self.role = role
        self.persona = persona
        self.messages = []
        self.api_key = os.getenv('OPENAI_API_KEY')

    def send_message(self, content):
        message = {"role": "assistant", "content": content}
        self.messages.append(message)
        return message

    def receive_message(self, content):
        message = {"role": "user", "content": content}
        self.messages.append(message)
        return message

    def generate_response(self, prompt):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages + [{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        reply = response['choices'][0]['message']['content']
        self.send_message(reply)
        return reply
