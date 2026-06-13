from tools import get_current_time, calculate_word_count, convert_to_uppercase
from planner import plan_action
from executor import execute_action

from config import (
    AGENT_NAME,
    AGENT_PERSONALITY,
    EXIT_COMMANDS,
    COMMAND_HELP,
    COMMAND_TIME,
    COMMAND_HISTORY,
    COMMAND_COUNT,
    COMMAND_UPPER,
)


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


def extract_text_after_command(command, command_name):
    words = command.split()

    if command_name not in words:
        return ""

    command_index = words.index(command_name)
    remaining_words = words[command_index + 1:]

    return " ".join(remaining_words)



def handle_command(command, conversation_history):
    action = plan_action(
        command,
        TOOLS,
        COMMAND_HELP,
        COMMAND_HISTORY,
        COMMAND_COUNT,
        COMMAND_UPPER,
    )

    result = execute_action(
        action,
        command,
        conversation_history,
        TOOLS,
        COMMAND_HELP,
        COMMAND_HISTORY,
        COMMAND_TIME,
        COMMAND_COUNT,
        COMMAND_UPPER,
        get_help_text,
        extract_text_after_command,
    )

    return respond_to_action_result(action, result, command)

def create_fallback_response(user_input):
    return f"{AGENT_NAME} ({AGENT_PERSONALITY}): You said: {user_input}"

def respond_to_action_result(action, result, user_input):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(user_input)

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