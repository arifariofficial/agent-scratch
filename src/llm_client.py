class LLMClient:
    def __init__(self, model_name, api_key=None):
        self.model_name = model_name
        self.api_key = api_key

    def ask(self, messages):
        if not self.api_key:
            return self._placeholder_response(messages)

        return self._real_llm_call(messages)

    def _placeholder_response(self, messages):
        return f"[{self.model_name}] placeholder response for messages: {messages}"

    def _real_llm_call(self, messages):
        return "Real LLM call not implemented yet"
