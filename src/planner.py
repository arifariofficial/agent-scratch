from llm_client import LLMClient
from llm_planner import build_planner_messages, parse_llm_plan
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
)


def contains_command(command, command_name):
    words = command.split()
    return command_name in words


def parse_intent(command, command_count, command_upper):
    if contains_command(command, command_count):
        return command_count

    if contains_command(command, command_upper):
        return command_upper

    return command


def plan_action_with_keywords(
    command,
    tools,
    command_help,
    command_history,
    command_count,
    command_upper,
):
    intent = parse_intent(command, command_count, command_upper)

    if intent in tools:
        return {
            "type": "tool",
            "tool_name": intent,
        }

    if intent in {command_help, command_history}:
        return {
            "type": "command",
            "command_name": intent,
        }

    return {
        "type": "fallback",
    }


def plan_action_with_llm(command, tools):
    llm = LLMClient(
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    )

    messages = build_planner_messages(command, tools)
    raw_response = llm.ask(messages)

    return parse_llm_plan(raw_response)


def is_valid_plan(action, tools, command_help, command_history):
    if action["type"] == "fallback":
        return True

    if action["type"] == "tool":
        return action.get("tool_name") in tools

    if action["type"] == "command":
        return action.get("command_name") in {command_help, command_history}

    return False


def plan_action(
    command, tools, command_help, command_history, command_count, command_upper
):
    action = plan_action_with_llm(command, tools)

    if is_valid_plan(action, tools, command_help, command_history):
        return action

    return plan_action_with_keywords(
        command,
        tools,
        command_help,
        command_history,
        command_count,
        command_upper,
    )
