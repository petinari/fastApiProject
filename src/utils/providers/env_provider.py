import os

from dotenv import load_dotenv

load_dotenv("/Users/robsonpetinari/PycharmProjects/fastApiProject/src/.env")


def get_value_env(key: str) -> str:
    value = os.getenv(key)
    if value:
        return value
    return ""
