def contains_command(command, command_name):
    words = command.split()
    return command_name in words


def parse_intent(command, command_count, command_upper):
    if contains_command(command, command_count):
        return command_count

    if contains_command(command, command_upper):
        return command_upper

    return command


def plan_action(command, tools, command_help, command_history, command_count, command_upper):
    intent = parse_intent(command, command_count, command_upper)

    if intent in tools:
        return {
            "type": "tool",
            "tool_name": intent,
        }

    if intent in {command_help, command_history}:
        return {
            "type": "command",
            "command_name": intent,
        }

    return {
        "type": "fallback",
    }