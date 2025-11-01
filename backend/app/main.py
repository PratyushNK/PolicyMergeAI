from fastapi import FastAPI
from app.core.database import engine, Base

app = FastAPI(title="Policy Merge API")

@app.on_event("startup")
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def root():
    return {"message": "Backend connected to Supabase Postgres successfully!"}
