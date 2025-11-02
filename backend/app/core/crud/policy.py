# app/core/crud/policy.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.policy import Policy
from app.schemas.policy_schema import PolicyCreate
from typing import List, Optional
import uuid

class PolicyCRUD:
    async def create_policy(self, db: AsyncSession, policy_in: PolicyCreate) -> Policy:
        policy = Policy(id=uuid.uuid4(), **policy_in.model_dump())
        db.add(policy)
        await db.commit()
        await db.refresh(policy)
        return policy

    async def get_policy(self, db: AsyncSession, policy_id: uuid.UUID) -> Optional[Policy]:
        result = await db.execute(select(Policy).where(Policy.id == policy_id))
        return result.scalar_one_or_none()

    async def get_all_policies(self, db: AsyncSession) -> List[Policy]:
        result = await db.execute(select(Policy))
        return result.scalars().all()

    async def delete_policy(self, db: AsyncSession, policy_id: uuid.UUID) -> bool:
        policy = await self.get_policy(db, policy_id)
        if not policy:
            return False
        await db.delete(policy)
        await db.commit()
        return True

policy_crud = PolicyCRUD()
