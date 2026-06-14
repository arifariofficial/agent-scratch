def build_fallback_messages(agent, user_input):
    messages = [
        {
            "role": "system",
            "content": (
                f"You are {agent.name}. "
                f"Personality: {agent.personality}. "
                "Use recent conversation history when helpful. "
                "Answer the latest user message clearly."
            ),
        }
    ]

    messages.extend(agent.get_recent_history())

    return messages


def build_final_answer_messages(agent, user_input, action, tool_result):
    return [
        {
            "role": "system",
            "content": (
                f"You are {agent.name}. "
                f"Personality: {agent.personality}. "
                "You are writing the final answer after a tool was used. "
                "Do not just repeat the raw tool result. "
                "Turn the tool result into a clear human answer. "
                "If the tool counted words, say how many words there are. "
                "If the tool uppercased text, show the uppercase text."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Original user request: {user_input}\n"
                f"Tool action: {action}\n"
                f"Tool result: {tool_result}\n\n"
                "Write the final answer to the user."
            ),
        },
    ]
