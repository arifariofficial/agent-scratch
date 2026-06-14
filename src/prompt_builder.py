def build_fallback_prompt(agent, user_input):
    return f"""
You are {agent.name}.
Personality: {agent.personality}

User message:
{user_input}

Respond helpfully and directly.
""".strip()
