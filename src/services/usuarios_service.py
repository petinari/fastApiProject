
from src.repositorios.usuario_repo import add_usuario


async def add_usuario_service(usuario_schema_in):
    return await add_usuario(usuario_schema_in)


#async def get_usuarios(usuario_schema_in):
 #   return await listar_usuarios(usuario_schema_in)

