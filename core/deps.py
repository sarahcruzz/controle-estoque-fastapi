import sys
default_path = "C:\\Users\\julia\\OneDrive\\Área de Trabalho\\backend"
sys.path.append(default_path)

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session # é um return "sem ser return" -> ele devolve a sessão, mas mantém a função viva
    finally:
        await session.close() # após utilizar a sessão com o banco de dados, ai sim, finalizamos ela    