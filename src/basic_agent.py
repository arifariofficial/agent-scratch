AGENT_NAME = "BasicAgent"
AGENT_PERSONALITY = "helpful and direct"

EXIT_COMMANDS = {"exit", "quit", "bye"}
AVAILABLE_COMMANDS = {"help", "time", "history", "count", "upper"}

def clean_input(user_input):
    return user_input.strip().lower()

def should_exit(user_input):
    return clean_input(user_input) in EXIT_COMMANDS

def get_current_time():
    return "Tool result: current time is not connected yet"

def calculate_word_count(text):
    words = text.split()
    return len(words)

def convert_to_uppercase(text):
    return text.upper()

def handle_command(command, conversation_history):
    if command == "help":
        return "Available commands: help, time, history, count <text>, upper <text>, exit"

    if command == "time":
        return get_current_time()

    if command == "history":
        return f"Conversation history: {conversation_history}"
    
    if command.startswith("count "):
        text_to_count = command.removeprefix("count ")
        word_count = calculate_word_count(text_to_count)
        return f"Word count: {word_count}"
    
    if command.startswith("upper "):
        text_to_convert = command.removeprefix("upper ")
        upper_text = convert_to_uppercase(text_to_convert)
        return f"Uppercase: {upper_text}"

    return None

def create_fallback_response(user_input):
    return f"{AGENT_NAME} ({AGENT_PERSONALITY}): You said: {user_input}"

def get_agent_response(user_input, conversation_history):
    cleaned_input = clean_input(user_input)

    command_response = handle_command(cleaned_input, conversation_history)

    if command_response:
        return command_response

    return create_fallback_response(user_input)


def main():
    conversation_history = []
    print(f"{AGENT_NAME} is ready. Type 'help' for commands.")

    while True:
        user_input = input("You: ")
        conversation_history.append(user_input)

        if should_exit(user_input):
            print("Goodbye")
            break

        print(get_agent_response(user_input, conversation_history))

if __name__ == "__main__":
    main()