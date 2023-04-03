

from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn
from src.config.database import database


usuario_collection = database.get_collection("usuarios_collection")

async def add_usuario(usuario_data: UsuarioSchemaIn):
    usuario = await usuario_collection.insert_one(usuario_data)
    #return await usuario_collection.find_one({"_id", usuario.inserted_id})
    return await usuario_collection.find_one({"_id": usuario.inserted_id})

