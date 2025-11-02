from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime import datetime

# --- PolicyVector Schemas ---
class PolicyVectorBase(BaseModel):
    embedding_vector: List[float]

class PolicyVectorCreate(PolicyVectorBase):
    id: UUID  # FK = Policy ID

class PolicyVectorRead(PolicyVectorBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True