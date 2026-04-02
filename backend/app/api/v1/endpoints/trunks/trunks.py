from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Trunk(BaseModel):
    id: str
    name: str
    provider: str
    sip_uri: str
    status: str  # active, inactive, degraded
    channels_max: int = 30
    channels_active: int = 0

@router.get("/", response_model=List[Trunk])
async def list_trunks():
    return []

@router.post("/", response_model=Trunk)
async def create_trunk(trunk: Trunk):
    return trunk

@router.delete("/{trunk_id}", status_code=204)
async def delete_trunk(trunk_id: str):
    pass
