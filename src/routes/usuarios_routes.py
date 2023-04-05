from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

from src.Schemas.usuarios.schemas_usuarios import (
    UsuarioSchemaIn,
    UsuarioSchemaOut,
    UsuarioLogin,
    Token, Usuario, )
from src.services.usuarios_service import UsuarioService
from src.utils.usuario.verifica_usuario_logado import verifica_usuario_logado

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=UsuarioSchemaOut)
async def post_usuario(usuario: UsuarioSchemaIn = Body(...)):
    return await UsuarioService().add_usuario_service(jsonable_encoder(usuario))


@router.post("/login", response_model=Token)
async def login_usuario(usuario: UsuarioLogin = Body(...)):
    token = await UsuarioService().login_usuario_service(usuario)
    if token is None:
        raise HTTPException(status_code=404, detail="Usuário e/ou senha incorretos.")
    return {"access_token": token, "token_type": "bearer"}


@router.get("/eu", response_model=Usuario)
async def read_users_me(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token"))]):
    return await verifica_usuario_logado(token)
