import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "BasicAgent"
AGENT_PERSONALITY = "helpful and direct"

LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "placeholder-model")
LLM_API_KEY = os.getenv("LLM_API_KEY")

EXIT_COMMANDS = {"exit", "quit", "bye"}

COMMAND_HELP = "help"
COMMAND_TIME = "time"
COMMAND_HISTORY = "history"
COMMAND_COUNT = "count"
COMMAND_UPPER = "upper"
