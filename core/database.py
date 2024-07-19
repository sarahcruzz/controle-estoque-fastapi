import sys
default_path = "C:\\Users\\julia\\OneDrive\\Área de Trabalho\\backend"
sys.path.append(default_path)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from core.configs import settings

engine = create_async_engine(settings.DB_URL, future=True, echo=True)

# sessionmaker retorna uma classe para nós!
# ele vai abrir e fechar a conexão com nosso banco de dados!
Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

Base = declarative_base()