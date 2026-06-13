from planner import plan_action
from executor import execute_action
from tool_registry import TOOLS
from responder import respond_to_action_result
from agent import Agent

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
    remaining_words = words[command_index + 1 :]

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

    return respond_to_action_result(
        action,
        result,
        command,
        AGENT_NAME,
        AGENT_PERSONALITY,
    )


def get_agent_response(user_input, conversation_history):
    cleaned_input = clean_input(user_input)
    return handle_command(cleaned_input, conversation_history)


def main():
    agent = Agent(AGENT_NAME, AGENT_PERSONALITY)

    while True:
        user_input = input("You: ")
        agent.remember(user_input)

        if should_exit(user_input):
            print("Goodbye")
            break

        print(get_agent_response(user_input, agent.conversation_history))


if __name__ == "__main__":
    main()
