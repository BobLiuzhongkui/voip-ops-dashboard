"""Pydantic schemas for Alert endpoints."""
from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field

from app.models.trunk import AlertSeverity

ChannelLiteral = Literal["email", "sms", "voice"]


class AlertCreate(BaseModel):
    severity: AlertSeverity
    channel: ChannelLiteral
    message: str = Field(..., min_length=1, max_length=2000)


class AlertResponse(BaseModel):
    id: int
    severity: AlertSeverity
    channel: str
    message: str
    created_at: datetime
    acknowledged: bool
    acknowledged_at: Optional[datetime] = None
    acknowledged_by: Optional[str] = None

    model_config = {"from_attributes": True}


class AlertListResponse(BaseModel):
    items: list[AlertResponse]
    total: int
