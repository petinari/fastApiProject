from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn, UsuarioLogin
from src.config.database import database


class UsuarioRepositorio:
    def __init__(self):
        self.usuario_collection = database.get_collection("usuarios_collection")

    async def add_usuario(self, usuario_in: UsuarioSchemaIn):
        usuario = await self.usuario_collection.insert_one(usuario_in)
        return await self.usuario_collection.find_one({"_id": usuario.inserted_id})

    async def get_usuario_por_nome(self, usuario: UsuarioLogin):
        us = await self.usuario_collection.find_one({"nome": usuario.nome})
        return us
