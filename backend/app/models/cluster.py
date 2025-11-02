# app/models/cluster.py
import uuid
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base


class Cluster(Base):
    __tablename__ = "cluster"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    size = Column(Integer)
    medoid = Column(UUID(as_uuid=True), ForeignKey("policy.id"), nullable=True)

    # Relationships
    policies = relationship(
        "Policy", 
        back_populates="cluster", 
        foreign_keys="Policy.cluster_id"
    )

    medoid_policy = relationship(
        "Policy",
        foreign_keys=[medoid],  # explicitly define medoid link
        uselist=False
    )
