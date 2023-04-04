from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn, UsuarioLogin
from src.repositorios.usuario_repo import UsuarioRepositorio
from src.utils.providers.hash_provider import gerar_hash


class UsuarioService:
    async def add_usuario_service(self, usuario: UsuarioSchemaIn):
        usuario['senha'] = gerar_hash(usuario['senha'])
        return await UsuarioRepositorio().add_usuario(usuario)

    async def get_usuarios_por_nome_service(self, usuario: UsuarioLogin):
        return await UsuarioRepositorio().get_usuario_por_nome(usuario)
