from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.Schemas.usuarios.schemas_usuarios import UsuarioSchemaIn, UsuarioSchemaOut, UsuarioLogin
from src.services.usuarios_service import UsuarioService

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)


@router.post('', response_model=UsuarioSchemaOut)
async def post_usuario(usuario: UsuarioSchemaIn = Body(...)):
    return await UsuarioService().add_usuario_service(jsonable_encoder(usuario))


@router.post('/login', response_model=UsuarioLogin)
async def login_usuario(usuario: UsuarioLogin = Body(...)):
    usuario_db = await UsuarioService().get_usuarios_por_nome_service(jsonable_encoder(usuario))
    return usuario_db
