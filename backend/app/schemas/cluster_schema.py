from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


# --- Cluster Schemas ---
class ClusterBase(BaseModel):
    size: Optional[int] = None
    medoid: Optional[UUID] = None

class ClusterCreate(ClusterBase):
    pass

class ClusterRead(ClusterBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
