from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_hash(texto_plano: str, texto_hashed: str)-> bool:
    return pwd_context.verify(texto_plano, texto_hashed)

def gerar_hash(texto_plano: str)-> str:
    return pwd_context.hash(texto_plano)