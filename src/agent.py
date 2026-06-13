class Agent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.conversation_history = []

    def remember(self, user_iniput):
        self.conversation_history.append(user_iniput)

    def get_welcome_message(self):
        return f"{self.name} is ready. Type 'help' for commands"

    def create_fallback_response(self, user_input):
        return f"{self.name} ({self.personality}): You said: {user_input}"

    def get_history(self):
        return self.conversation_history

    def should_exit(self, user_input, exit_commands):
        return user_input.strip().lower() in exit_commands
