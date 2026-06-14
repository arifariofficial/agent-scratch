import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "BasicAgent"
AGENT_PERSONALITY = "helpful and direct"

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

EXIT_COMMANDS = {"exit", "quit", "bye"}

COMMAND_HELP = "help"
COMMAND_TIME = "time"
COMMAND_HISTORY = "history"
COMMAND_COUNT = "count"
COMMAND_UPPER = "upper"


MEMORY_MESSAGE_LIMIT = 8
