from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import engine, Base, get_session
from app.models import policy as policy_model, cluster as cluster_model, policy_vector as policy_vector_model
from app.models.policy import Policy
from app.schemas.policy_schema import PolicyCreate
from app.api.routes import policy, cluster, policy_vector


app = FastAPI(title="Policy Merge API")

@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(policy.router)
app.include_router(cluster.router)
app.include_router(policy_vector.router)

@app.get("/")
def root():
    return {"message": "Backend connected to Supabase Postgres successfully!"}
