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
    COMMAND_TIME: {
        "function": get_current_time,
        "description": "Returns the current time",
        "example": "time",
    },
    COMMAND_COUNT: {
        "function": calculate_word_count,
        "description": "Counts words in text",
        "example": "count hello world",
    },
    COMMAND_UPPER: {
        "function": convert_to_uppercase,
        "description": "Converts text to uppercase",
        "example": "upper hello world",
    },
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
    lines = ["Available commands:"]

    lines.append("- help: Shows available commands")
    lines.append("- history: Shows conversation history")

    for tool_name, tool_info in TOOLS.items():
        description = tool_info["description"]
        example = tool_info["example"]
        lines.append(f"- {tool_name}: {description} | Example: {example}")

    lines.append("- exit: Stops the agent")

    return "\n".join(lines)

def is_count_command(command):
    return command.startswith(f"{COMMAND_COUNT} ")

def is_upper_command(command):
    return command.startswith(f"{COMMAND_UPPER} ")

def handle_command(command, conversation_history):
    if command == COMMAND_HELP:
        return get_help_text()

    if command == COMMAND_TIME:
        tool = TOOLS[COMMAND_TIME]["function"]
        return tool()

    if command == COMMAND_HISTORY:
        return f"Conversation history: {conversation_history}"
    
    if is_count_command(command):
        text_to_count = command.removeprefix("count ")
        tool = TOOLS[COMMAND_COUNT]["function"]
        word_count = tool(text_to_count)
        return f"Word count: {word_count}"
    
    if is_upper_command(command):
        text_to_convert = command.removeprefix("upper ")
        tool = TOOLS[COMMAND_UPPER]["function"]
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