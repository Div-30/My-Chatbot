import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
MODEL_NAME = "claude-haiku-4-5"

messages = []

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def stream_chat(messages, system_prompt=None):
    params = {
        "model": MODEL_NAME,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system_prompt:
        params["system"] = system_prompt
        
    return client.messages.stream(**params)