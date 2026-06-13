def execute_tool(tool_name, tools, text=""):
    tool = tools[tool_name]["function"]

    if text:
        return tool(text)

    return tool()