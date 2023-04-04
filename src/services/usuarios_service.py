from datetime import timedelta

from src.Schemas.usuarios.schemas_usuarios import UsuarioLogin
from src.repositorios.usuario_repo import UsuarioRepositorio
from src.utils.providers.hash_provider import gerar_hash, verificar_hash
from src.utils.providers.token_provider import criar_token_acesso


class UsuarioService:
    async def add_usuario_service(self, usuario):
        usuario["senha"] = gerar_hash(usuario["senha"])
        return await UsuarioRepositorio().add_usuario(usuario)

    async def login_usuario(self, usuario: UsuarioLogin):
        usuario_db = await UsuarioRepositorio().get_usuario_por_nome(usuario)
        if usuario_db is not None:
            if not verificar_hash(usuario.senha, usuario_db['senha']):
                return None
        access_token_expires = timedelta(minutes=360)
        access_token = criar_token_acesso(
            data={"sub": usuario_db['nome']}, expires_delta=access_token_expires
        )
        return access_token
