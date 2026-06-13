class Agent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.conversation_history = []

    def remember(self, user_iniput):
        self.conversation_history.append(user_iniput)

    def get_welcome_message(self):
        return f"{self.name} is ready. Type 'help' for commands"
