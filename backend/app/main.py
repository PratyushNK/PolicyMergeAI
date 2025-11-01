from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import engine, Base, get_session
from app.models.policy import Policy
from app.schemas.policy_schema import PolicyCreate

app = FastAPI(title="Policy Merge API")

@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def root():
    return {"message": "Backend connected to Supabase Postgres successfully!"}


@app.post("/policies/")
async def create_policy(payload: PolicyCreate, session: AsyncSession = Depends(get_session)):
    policy = Policy(name=payload.name, content=payload.content)
    session.add(policy)
    await session.commit()
    await session.refresh(policy)
    return policy


@app.get("/policies/")
async def list_policies(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Policy))
    policies = result.scalars().all()
    return policies
