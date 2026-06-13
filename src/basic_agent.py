from tools import get_current_time, calculate_word_count, convert_to_uppercase


AGENT_NAME = "BasicAgent"
AGENT_PERSONALITY = "helpful and direct"

EXIT_COMMANDS = {"exit", "quit", "bye"}



COMMAND_HELP = "help"
COMMAND_TIME = "time"
COMMAND_HISTORY = "history"
COMMAND_COUNT = "count"
COMMAND_UPPER = "upper"


TOOLS = {
    COMMAND_TIME: get_current_time,
    COMMAND_COUNT: calculate_word_count,
    COMMAND_UPPER: convert_to_uppercase,
}

AVAILABLE_COMMANDS = {
    COMMAND_HELP,
    COMMAND_TIME,
    COMMAND_HISTORY,
    COMMAND_COUNT,
    COMMAND_UPPER,
}



def clean_input(user_input):
    return user_input.strip().lower()

def should_exit(user_input):
    return clean_input(user_input) in EXIT_COMMANDS

def get_help_text():
    return "Available commands: help, time, history, count <text>, upper <text>, exit"

def is_count_command(command):
    return command.startswith(f"{COMMAND_COUNT} ")

def is_upper_command(command):
    return command.startswith(f"{COMMAND_UPPER} ")

def handle_command(command, conversation_history):
    if command == COMMAND_HELP:
        return get_help_text()

    if command == COMMAND_TIME:
        tool = TOOLS[COMMAND_TIME]
        return tool()

    if command == COMMAND_HISTORY:
        return f"Conversation history: {conversation_history}"
    
    if is_count_command(command):
        text_to_count = command.removeprefix("count ")
        tool = TOOLS[COMMAND_COUNT]
        word_count = tool(text_to_count)
        return f"Word count: {word_count}"
    
    if is_upper_command(command):
        text_to_convert = command.removeprefix("upper ")
        tool = TOOLS[COMMAND_UPPER]
        upper_text = tool(text_to_convert)
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