import json


def build_planner_messages(user_input, tools):
    tool_names = ", ".join(tools.keys())

    return [
        {
            "role": "system",
            "content": (
                "You are a strict planner for an AI agent. "
                "Return only valid JSON. No explanation. "
                "Only choose a tool when the user clearly asks for that tool's job. "
                "For normal conversation, always return fallback."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Available tools: {tool_names}\n"
                f"User input: {user_input}\n\n"
                "Tool rules:\n"
                "- Use count only when the user asks to count words.\n"
                "- Use upper only when the user asks to uppercase, capitalize, or convert text to uppercase.\n"
                "- Use time only when the user asks for time.\n"
                "- Otherwise use fallback.\n\n"
                "When using count or upper, include args.text with the exact text to process.\n\n"
                "Return exactly one JSON object:\n"
                '{"type": "tool", "tool_name": "count", "args": {"text": "text to count"}}\n'
                '{"type": "tool", "tool_name": "upper", "args": {"text": "text to uppercase"}}\n'
                '{"type": "tool", "tool_name": "time", "args": {}}\n'
                '{"type": "fallback"}'
            ),
        },
    ]


def parse_llm_plan(raw_response):
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        return {"type": "fallback"}
