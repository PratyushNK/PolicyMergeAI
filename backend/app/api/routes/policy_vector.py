from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.core.crud.policy_vector import policy_vector_crud
from app.schemas.policy_vector_schema import PolicyVectorCreate, PolicyVectorRead

router = APIRouter(prefix="/policy_vector", tags=["PolicyVector"])


@router.post("/", response_model=PolicyVectorRead)
async def create_policy_vector(data: PolicyVectorCreate, session: AsyncSession = Depends(get_session)):
    return await policy_vector_crud.create_policy_vector(session, data)


@router.get("/{policy_vector_id}", response_model=PolicyVectorRead)
async def get_policy_vector(policy_vector_id: str, session: AsyncSession = Depends(get_session)):
    vector = await policy_vector_crud.get_policy_vector(session, policy_vector_id)
    if not vector:
        raise HTTPException(status_code=404, detail="PolicyVector not found")
    return vector


@router.get("/", response_model=list[PolicyVectorRead])
async def list_policy_vectors(session: AsyncSession = Depends(get_session)):
    return await policy_vector_crud.list_policy_vectors(session)


@router.delete("/{policy_vector_id}")
async def delete_policy_vector(policy_vector_id: str, session: AsyncSession = Depends(get_session)):
    await policy_vector_crud.delete_policy_vector(session, policy_vector_id)
    return {"message": f"PolicyVector {policy_vector_id} deleted"}
