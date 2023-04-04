import os
from datetime import timedelta, datetime
from typing import Union

from dotenv import load_dotenv
from jose import jwt

load_dotenv('/Users/robsonpetinari/PycharmProjects/fastApiProject/src/.env')


def criar_token_acesso(data: dict, expires_delta: Union[timedelta, None] = None):
    print(os.getenv('SECRET_KEY'), "----", os.getenv('ALGORITHM'))
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt
