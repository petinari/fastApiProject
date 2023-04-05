from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from starlette import status

from src.Schemas.usuarios.schemas_usuarios import Usuario
from src.services.usuarios_service import UsuarioService
from src.utils.providers.jwt_decoder_provider import decode_jwt_token


async def verifica_usuario_logado(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possivel validar a credencial.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt_token(token)
        nome: str = payload.get("sub")
        if nome is None:
            raise credentials_exception
        usuario = Usuario(nome=nome)
    except JWTError:
        raise credentials_exception
    user = await UsuarioService().get_usuario_por_nome_service(usuario)
    if user is None:
        raise credentials_exception
    return user
