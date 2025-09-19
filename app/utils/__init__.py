import os, string, random


def enabled(key: str) -> bool:
    return os.getenv(key, "false").lower() in ["true", "1", "yes"]


def random_code(length: int = 6) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
