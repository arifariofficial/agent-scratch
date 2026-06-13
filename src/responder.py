def create_fallback_response(agent, user_input):
    return agent.create_fallback_response(user_input)


def respond_to_action_result(action, result, user_input, agent):
    if action["type"] == "tool":
        return str(result)

    if action["type"] == "command":
        return str(result)

    return create_fallback_response(agent, user_input)
