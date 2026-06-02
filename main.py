from chatbot_engine import messages, add_user_message, add_assistant_message, stream_chat

system_message = "You are a helpful AI assistant."

print("Chatbot Initialized! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
        
    add_user_message(messages, user_input)
    
    print("Claude: ", end="")
    with stream_chat(messages, system_prompt=system_message) as stream:
        for text in stream.text_stream:
            print(text, end="")
            
    final_msg = stream.get_final_message()
    add_assistant_message(messages, final_msg.content[0].text)
    print("\n")