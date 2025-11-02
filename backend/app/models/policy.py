# app/models/policy.py
import uuid
from sqlalchemy import Column, String, Text, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone


class Policy(Base):
    __tablename__ = "policy"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_type = Column(String)
    subject_name = Column(String)
    subject_attributes = Column(JSON)
    resource_type = Column(String)
    resource_name = Column(String)
    resource_attributes = Column(JSON)
    action_name = Column(String)
    effect = Column(String)
    condition = Column(JSON)
    policy_model = Column(String)
    owner_name = Column(String)
    original_policy = Column(String)
    cluster_id = Column(UUID(as_uuid=True), ForeignKey("cluster.id"))
    source_company_name = Column(String)
    derived_from = Column(JSON)
    policy_type = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    cluster = relationship(
        "Cluster",
        back_populates="policies",
        foreign_keys=[cluster_id]  # explicitly define which FK connects to Cluster
    )

    policy_vector = relationship(
        "PolicyVector", 
        back_populates="policy", 
        uselist=False 
    )
