from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.core.crud.cluster import ClusterCRUD as cluster_crud
from app.schemas.cluster_schema import ClusterCreate, ClusterRead

router = APIRouter(prefix="/cluster", tags=["Cluster"])


@router.post("/", response_model=ClusterRead)
async def create_cluster(data: ClusterCreate, session: AsyncSession = Depends(get_session)):
    return await cluster_crud.create_cluster(session, data)


@router.get("/{cluster_id}", response_model=ClusterRead)
async def get_cluster(cluster_id: str, session: AsyncSession = Depends(get_session)):
    cluster = await cluster_crud.get_cluster(session, cluster_id)
    if not cluster:
        raise HTTPException(status_code=404, detail="Cluster not found")
    return cluster


@router.get("/", response_model=list[ClusterRead])
async def list_clusters(session: AsyncSession = Depends(get_session)):
    return await cluster_crud.get_all_clusters(session)


@router.delete("/{cluster_id}")
async def delete_cluster(cluster_id: str, session: AsyncSession = Depends(get_session)):
    await cluster_crud.delete_cluster(session, cluster_id)
    return {"message": f"Cluster {cluster_id} deleted"}
