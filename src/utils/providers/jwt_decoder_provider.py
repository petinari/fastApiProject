from jose import jwt

from src.utils.providers.env_provider import get_value_env


def decode_jwt_token(token):
    return jwt.decode(token, get_value_env("SECRET_KEY"), get_value_env("ALGORITHM"))
