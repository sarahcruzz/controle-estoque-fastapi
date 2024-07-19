import sys
default_path = "C:\\Users\\ct67ca\Desktop\\learning_api\\projeto_sqlAlchemy"
sys.path.append(default_path)

from fastapi import APIRouter
from api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/funcionarios', tags=["funcionarios"])
# /api/v1/cursos -> esse será nosso endpoint completo junto ao prefixo!