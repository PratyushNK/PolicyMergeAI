from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.cluster import Cluster
from app.schemas.cluster_schema import ClusterCreate
from typing import List, Optional
import uuid


class ClusterCRUD:
    @staticmethod
    async def create_cluster(db: AsyncSession, cluster_in: ClusterCreate) -> Cluster:
        cluster = Cluster(id=uuid.uuid4(), **cluster_in.model_dump())
        db.add(cluster)
        await db.commit()
        await db.refresh(cluster)
        return cluster

    @staticmethod
    async def get_cluster(db: AsyncSession, cluster_id: uuid.UUID) -> Optional[Cluster]:
        result = await db.execute(select(Cluster).where(Cluster.id == cluster_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all_clusters(db: AsyncSession) -> List[Cluster]:
        result = await db.execute(select(Cluster))
        return result.scalars().all()

    @staticmethod
    async def delete_cluster(db: AsyncSession, cluster_id: uuid.UUID) -> bool:
        cluster = await ClusterCRUD.get_cluster(db, cluster_id)
        if not cluster:
            return False
        await db.delete(cluster)
        await db.commit()
        return True
