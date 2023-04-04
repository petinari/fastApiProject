from pydantic import Field

from src.Schemas.base_model_app import BaseModelApp
from src.utils.pyObjectId import PyObjectId


class UsuarioSchemaIn(BaseModelApp):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nome: str
    senha: str


class UsuarioSchemaOut(BaseModelApp):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nome: str


class UsuarioLogin(BaseModelApp):
    nome: str
    senha: str


class Token(BaseModelApp):
    access_token: str
    token_type: str
