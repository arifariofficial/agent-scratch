def create_fallback_response(agent_name, agent_personality, user_input):
    return f"{agent_name} ({agent_personality}): You said: {user_input}"


def respond_to_action_result(action, result, user_input, agent_name, agent_personality):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent_name, agent_personality, user_input)