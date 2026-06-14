def build_fallback_messages(agent, user_input):
    messages = [
        {
            "role": "system",
            "content": f"You are {agent.name}. Personality: {agent.personality}. Respond helpfully and directly.",
        }
    ]

    for previous_user_input in agent.get_history()[-5:]:
        messages.append(
            {
                "role": "user",
                "content": previous_user_input,
            }
        )

    return messages
