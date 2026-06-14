def format_tool_result(tool_result):
    if not isinstance(tool_result, dict):
        return str(tool_result)

    tool_name = tool_result.get("tool_name", "unknown")
    tool_input = tool_result.get("input", "")
    tool_output = tool_result.get("output", "")

    return (
        f"Tool name: {tool_name}\nTool input: {tool_input}\nTool output: {tool_output}"
    )
