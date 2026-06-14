from llm_client import LLMClient
from config import LLM_MODEL_NAME
from prompt_builder import build_fallback_prompt


def create_fallback_response(agent, user_input):
    prompt = build_fallback_prompt(agent, user_input)
    llm = LLMClient(LLM_MODEL_NAME)
    return llm.ask(prompt)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
