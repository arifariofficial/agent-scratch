def get_agent_response(user_input, conversation_history):
    cleaned_input = user_input.strip().lower()

    if cleaned_input == "help":
        return "Available commands: help, exit"
    
    if cleaned_input == "time":
        return "I cannot check the time yet, but later i will use a tool for this."
    
    if cleaned_input == "history":
        return f"Conversation history: {conversation_history}"
    
    return f"You said: {user_input}"


def main():
    conversation_history = []

    while True:
        user_input = input("You: ")

        conversation_history.append(user_input)

        if user_input.strip() in {"exit", "quit", "bye"}:
            print("Goodbye")
            break

        print(get_agent_response(user_input, conversation_history))

if __name__ == "__main__":
    main()