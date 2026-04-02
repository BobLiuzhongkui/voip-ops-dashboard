"""Pydantic schemas for Trunk endpoints."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from app.models.trunk import TrunkStatus


class TrunkBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    provider: str = Field(..., min_length=1, max_length=100)
    sip_uri: str = Field(..., min_length=1, max_length=255)
    username: Optional[str] = Field(None, max_length=100)
    channels_max: int = Field(30, ge=1, le=1000)


class TrunkCreate(TrunkBase):
    pass


class TrunkUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    provider: Optional[str] = Field(None, min_length=1, max_length=100)
    sip_uri: Optional[str] = Field(None, min_length=1, max_length=255)
    username: Optional[str] = Field(None, max_length=100)
    channels_max: Optional[int] = Field(None, ge=1, le=1000)
    status: Optional[TrunkStatus] = None


class TrunkResponse(TrunkBase):
    id: int
    status: TrunkStatus
    channels_active: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TrunkListResponse(BaseModel):
    items: list[TrunkResponse]
    total: int
