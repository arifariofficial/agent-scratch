from llm_client import LLMClient
from config import LLM_MODEL_NAME, LLM_API_KEY
from prompt_builder import build_fallback_messages


def create_fallback_response(agent, user_input):
    messages = build_fallback_messages(agent, user_input)
    llm = LLMClient(LLM_MODEL_NAME, LLM_API_KEY)
    return llm.ask(messages)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
