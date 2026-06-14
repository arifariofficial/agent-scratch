from llm_client import ask_llm


def create_fallback_response(agent, user_input):
    prompt = f"You are {agent.name}. Personality: {agent.personality}. User said: {user_input}"
    return ask_llm(prompt)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
