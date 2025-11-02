from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import get_settings

settings = get_settings()

# Disable prepared statements entirely for PgBouncer (transaction mode)
connect_args = {
    # asyncpg specific
    "statement_cache_size": 0,
    "prepared_statement_cache_size": 0,
    "server_settings": {
        "statement_timeout": "60000",
        "statement_cache_size": "0",
        "prepared_statement_cache_size": "0",
    }
}

# Create engine
engine = create_async_engine(
    settings.database_url,
    echo=False,
    future=True,
    pool_pre_ping=True,
    connect_args=connect_args,
)

# Create session factory
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for all ORM models
Base = declarative_base()

# Dependency for routes
async def get_session():
    async with async_session() as session:
        yield session
