import sys
default_path = "C:\\Users\\ct67ca\Desktop\\learning_api\\projeto_sqlAlchemy"
sys.path.append(default_path)

from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession # Serve para tipar dados
from sqlalchemy.future import select # forçar o slqalchemy a usar o modelo mais recente da orm que é o 2.0

from models.user_model import CursoModel # validação de dados
from schemas.user_schema import UserSchema # 
from core.deps import get_session

# vou responder um CursoSchema e também receber um CursoSchema!
# API envia JSON e espera receber um JSON
router = APIRouter()

# POST CURSOS
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo = curso.titulo,
                            aulas = curso.aulas,
                            horas = curso.horas,
                            instrutor = curso.instrutor,)
    db.add(novo_curso)
    await db.commit()
    return novo_curso

# GET Cursos
@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos
    
# GET Curso (individual)
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session: 
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado..."))
        
# PUT Curso
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas
            curso_up.instrutor = curso.instrutor
            await session.commit()
            return curso_up
        else: 
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado..."))
        
# DELETE Curso
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()
        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado..."))