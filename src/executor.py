def execute_tool(tool_name, tools, text=""):
    tool = tools[tool_name]["function"]

    if text:
        raw_result = tool(text)
    else:
        raw_result = tool()

    return {
        "tool_name": tool_name,
        "input": text,
        "output": raw_result,
    }


def execute_action(
    action,
    command,
    conversation_history,
    tools,
    command_help,
    command_history,
    command_time,
    command_count,
    command_upper,
    get_help_text,
    extract_text_after_command,
):
    if action["type"] == "command" and action["command_name"] == command_help:
        return get_help_text()

    if action["type"] == "command" and action["command_name"] == command_history:
        return f"Conversation history: {conversation_history}"

    if action["type"] == "tool" and action["tool_name"] == command_time:
        return execute_tool(command_time, tools)

    if action["type"] == "tool" and action["tool_name"] == command_count:
        text_to_count = action.get("args", {}).get("text")

        if not text_to_count:
            text_to_count = extract_text_after_command(command, command_count)

        return execute_tool(command_count, tools, text_to_count)

    if action["type"] == "tool" and action["tool_name"] == command_upper:
        text_to_convert = action.get("args", {}).get("text")

        if not text_to_convert:
            text_to_convert = extract_text_after_command(command, command_upper)

        return execute_tool(command_upper, tools, text_to_convert)

    return None
