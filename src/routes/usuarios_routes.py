from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn, UsuarioSchemaOut, UsuarioLogin, Token
from src.services.usuarios_service import UsuarioService

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)


@router.post('', response_model=UsuarioSchemaOut)
async def post_usuario(usuario: UsuarioSchemaIn = Body(...)):
    return await UsuarioService().add_usuario_service(jsonable_encoder(usuario))


@router.post('/login', response_model=Token)
async def login_usuario(usuario: UsuarioLogin = Body(...)):
    token = await UsuarioService().login_usuario(usuario)
    if token is None:
        raise HTTPException(status_code=404, detail="Usuário e/ou senha incorretos.")
    return {"access_token": token, "token_type": "bearer"}
