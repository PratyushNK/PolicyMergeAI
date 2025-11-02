from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.core.crud.policy import policy_crud
from app.schemas.policy_schema import PolicyCreate, PolicyRead

router = APIRouter(prefix="/policy", tags=["Policy"])


@router.post("/", response_model=PolicyRead)
async def create_policy(data: PolicyCreate, session: AsyncSession = Depends(get_session)):
    return await policy_crud.create_policy(session, data)


@router.get("/{policy_id}", response_model=PolicyRead)
async def get_policy(policy_id: str, session: AsyncSession = Depends(get_session)):
    policy = await policy_crud.get_policy(session, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy


@router.get("/", response_model=list[PolicyRead])
async def list_policies(session: AsyncSession = Depends(get_session)):
    return await policy_crud.list_policies(session)


@router.delete("/{policy_id}")
async def delete_policy(policy_id: str, session: AsyncSession = Depends(get_session)):
    await policy_crud.delete_policy(session, policy_id)
    return {"message": f"Policy {policy_id} deleted"}
