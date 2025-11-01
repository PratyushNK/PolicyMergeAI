from pydantic import BaseModel
from typing import Optional

class PolicyCreate(BaseModel):
    name: str
    content: Optional[str] = None
