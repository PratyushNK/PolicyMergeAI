# app/models/policy_vector.py
import uuid
from sqlalchemy import Column, ForeignKey, ARRAY, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base


class PolicyVector(Base):
    __tablename__ = "policy_vectors"

    id = Column(UUID(as_uuid=True), ForeignKey("policies.id"), primary_key=True)
    embedding = Column(ARRAY(Float, dimensions=1))  # 384-d vector

    # Relationships
    policy = relationship("Policy", back_populates="policy_vector")
