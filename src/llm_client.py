from openai import OpenAI


class LLMClient:
    def __init__(
        self,
        endpoint=None,
        api_key=None,
        deployment_name=None,
        api_version="preview",
    ):
        self.endpoint = endpoint
        self.api_key = api_key
        self.deployment_name = deployment_name
        self.api_version = api_version

    def ask(self, messages):
        if not self.endpoint or not self.api_key or not self.deployment_name:
            return self._placeholder_response(messages)

        return self._real_llm_call(messages)

    def _placeholder_response(self, messages):
        model_name = self.deployment_name or "no-model-configured"
        return f"[{model_name}] placeholder response for messages: {messages}"

    def _real_llm_call(self, messages):
        if self.endpoint is None:
            raise ValueError("AZURE_OPENAI_ENDPOINT is missing")

        if self.api_key is None:
            raise ValueError("AZURE_OPENAI_API_KEY is missing")

        if self.deployment_name is None:
            raise ValueError("AZURE_OPENAI_DEPLOYMENT_NAME is missing")

        client = OpenAI(
            base_url=self.endpoint,
            api_key=self.api_key,
            default_query={"api-version": self.api_version},
        )

        response = client.responses.create(
            model=self.deployment_name,
            input=messages,
        )

        return response.output_text
