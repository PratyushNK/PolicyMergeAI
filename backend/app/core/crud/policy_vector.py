from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.policy_vector import PolicyVector
from app.schemas.policy_vector_schema import PolicyVectorCreate
from typing import List, Optional
import uuid

class PolicyVectorCRUD:
    async def create_policy_vector(db: AsyncSession, pv_in: PolicyVectorCreate) -> PolicyVector:
        policy_vector = PolicyVector(id=uuid.uuid4(), **pv_in.model_dump())
        db.add(policy_vector)
        await db.commit()
        await db.refresh(policy_vector)
        return policy_vector

    async def get_policy_vector(db: AsyncSession, pv_id: uuid.UUID) -> Optional[PolicyVector]:
        result = await db.execute(select(PolicyVector).where(PolicyVector.id == pv_id))
        return result.scalar_one_or_none()

    async def get_all_policy_vectors(db: AsyncSession) -> List[PolicyVector]:
        result = await db.execute(select(PolicyVector))
        return result.scalars().all()

    async def delete_policy_vector(db: AsyncSession, pv_id: uuid.UUID) -> bool:
        pv = await get_policy_vector(db, pv_id)
        if not pv:
            return False
        await db.delete(pv)
        await db.commit()
        return True

policy_vector_crud = PolicyVectorCRUD()