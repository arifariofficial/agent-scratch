from debug_logger import debug_log
from llm_client import LLMClient
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
)
from prompt_builder import build_fallback_messages, build_final_answer_messages


def create_llm_client():
    return LLMClient(
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    )


def create_fallback_response(agent, user_input):
    messages = build_fallback_messages(agent, user_input)

    debug_log("Fallback response messages", messages)

    llm = create_llm_client()
    return llm.ask(messages)


def create_tool_response(agent, user_input, action, tool_result):
    messages = build_final_answer_messages(agent, user_input, action, tool_result)

    debug_log("Final response messages", messages)

    llm = create_llm_client()
    return llm.ask(messages)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return create_tool_response(agent, user_input, action, result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
