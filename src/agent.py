class Agent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.conversation_history = []

    def remember_user_message(self, user_input):
        self.conversation_history.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

    def remember_assistant_message(self, assistant_output):
        self.conversation_history.append(
            {
                "role": "assistant",
                "content": assistant_output,
            }
        )

    def get_history(self):
        return self.conversation_history

    def get_recent_history(self, limit=6):
        return self.conversation_history[-limit:]

    def get_welcome_message(self):
        return f"{self.name} is ready. Type 'help' for commands."

    def create_fallback_response(self, user_input):
        return f"{self.name} ({self.personality}): You said: {user_input}"

    def should_exit(self, user_input, exit_commands):
        return user_input.strip().lower() in exit_commands
