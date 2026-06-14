class LLMClient:
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, messages):
        return f"[{self.model_name}] response placeholder for messages: {messages}"
