from config import DEBUG_MODE


def debug_log(label, value):
    if not DEBUG_MODE:
        return

    print(f"[DEBUG] {label}: {value}")
