def build_fallback_messages(agent, user_input):
    return [
        {
            "role": "system",
            "content": f"You are {agent.name}. Personality: {agent.personality}. Respond helpfully and directly.",
        },
        {
            "role": "user",
            "content": user_input,
        },
    ]
