from config import COMMAND_TIME, COMMAND_COUNT, COMMAND_UPPER
from tools import get_current_time, calculate_word_count, convert_to_uppercase


TOOLS = {
    COMMAND_TIME: {
        "function": get_current_time,
        "description": "Returns the current time",
        "example": "time",
    },
    COMMAND_COUNT: {
        "function": calculate_word_count,
        "description": "Counts words in text",
        "example": "count hello world",
    },
    COMMAND_UPPER: {
        "function": convert_to_uppercase,
        "description": "Converts text to uppercase",
        "example": "upper hello world",
    },
}