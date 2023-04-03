from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn, UsuarioSchemaOut


from src.services import usuarios_service

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)

@router.post('', response_model=UsuarioSchemaOut)
async def post_usuario(usuario: UsuarioSchemaIn = Body(...)):
    usuario = jsonable_encoder(usuario)
    return await usuarios_service.add_usuario(usuario)

