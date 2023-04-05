from datetime import timedelta, datetime
from typing import Union

from jose import jwt

from src.utils.providers.env_provider import get_value_env


def criar_token_acesso(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, key=get_value_env("SECRET_KEY"), algorithm=get_value_env("ALGORITHM")
    )
    return encoded_jwt
