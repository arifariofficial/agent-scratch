from llm_client import LLMClient
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
)
from prompt_builder import build_fallback_messages


def create_fallback_response(agent, user_input):
    messages = build_fallback_messages(agent, user_input)

    llm = LLMClient(
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    )

    return llm.ask(messages)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
