"""Pydantic schemas for Monitoring endpoints."""
from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, Field


class ChannelMetricsResponse(BaseModel):
    channel: str
    active_connections: int = 0
    pending: int = 0
    completed: int = 0
    failed: int = 0
    avg_response_time_ms: float = 0.0
    recorded_at: datetime

    model_config = {"from_attributes": True}


class MonitoringSummaryResponse(BaseModel):
    overview: Dict[str, float]
    channels: List[ChannelMetricsResponse]
    alerts_count: int


class MetricHistoryPoint(BaseModel):
    recorded_at: datetime
    active_connections: int
    completed: int
    failed: int
    avg_response_time_ms: float


class ChannelHistoryResponse(BaseModel):
    channel: str
    points: List[MetricHistoryPoint]
