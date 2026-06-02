# My-Chatbot

A lightweight interactive chatbot powered by Claude AI using the Anthropic API with real-time streaming responses.

## Overview

My-Chatbot is a simple yet functional terminal-based conversational AI assistant. It maintains conversation context and provides real-time streaming responses from Claude Haiku, making interactions feel natural and responsive.

## Features

- **Real-time streaming**: See AI responses as they're generated
- **Conversation memory**: Maintains chat history within a session
- **Easy setup**: Simple configuration with environment variables
- **Interactive CLI**: Clean terminal interface for chatting

## Project Structure

```
My-Chatbot/
├── main.py                  # Entry point - interactive chatbot loop
├── chatbot_engine.py        # Core engine - API integration and message handling
├── .env.example             # Template for API configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Getting Started

### Prerequisites

- Python 3.7+
- Anthropic API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install anthropic python-dotenv
   ```

3. Configure your API key:
   - Copy `.env.example` to `.env`
   - Add your Anthropic API key: `ANTHROPIC_API_KEY=your_key_here`

### Usage

Run the chatbot:
```bash
python main.py
```

Then start typing to chat. Type `exit` to quit.

## How It Works

- **main.py**: Handles the interactive loop, taking user input and displaying streamed responses
- **chatbot_engine.py**: Manages API calls to Claude Haiku, maintains message history, and handles streaming

The chatbot uses a configurable system prompt (currently set to "You are a helpful AI assistant") and maintains full conversation context for coherent multi-turn dialogues.
