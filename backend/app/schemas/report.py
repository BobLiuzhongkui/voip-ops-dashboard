"""Pydantic schemas for Report endpoints."""
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field

PeriodLiteral = Literal["daily", "weekly", "monthly"]


class ReportSummaryResponse(BaseModel):
    period: PeriodLiteral
    total_calls: int = 0
    total_messages: int = 0
    avg_response_time_ms: float = 0.0
    success_rate: float = 0.0
    generated_at: datetime


class ChannelDataPoint(BaseModel):
    timestamp: datetime
    completed: int
    failed: int
    avg_response_time_ms: float


class ChannelReportResponse(BaseModel):
    channel: str
    start: Optional[datetime]
    end: Optional[datetime]
    data: List[ChannelDataPoint]
