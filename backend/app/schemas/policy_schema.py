from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from uuid import UUID
from datetime import datetime

# --- Policy Schemas ---
class PolicyBase(BaseModel):
    subject_type: str
    subject_name: str
    subject_attributes: Optional[Dict[str, str]] = None
    resource_type: str
    resource_name: str
    resource_attributes: Optional[Dict[str, str]] = None
    action_name: str
    effect: str
    condition: Optional[Dict[str, str]] = None
    policy_model: str
    owner_name: str
    original_policy: Optional[str] = None
    cluster_id: Optional[UUID] = None
    source_company_name: Optional[str] = None
    derived_from: Optional[List[UUID]] = None
    policy_type: Optional[str] = Field(default="original")

class PolicyCreate(PolicyBase):
    pass

class PolicyRead(PolicyBase):
    id: UUID

    class Config:
        orm_mode = True