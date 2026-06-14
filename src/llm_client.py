class LLMClient:
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, prompt):
        return f"[{self.model_name}] response placeholder for: {prompt}"
