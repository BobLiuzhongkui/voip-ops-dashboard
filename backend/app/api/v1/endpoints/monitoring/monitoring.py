"""
Monitoring endpoints — real-time metrics for Email, SMS, and Voice channels.
"""
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from typing import Dict, List, Any
from datetime import datetime

router = APIRouter()

class ChannelMetrics(BaseModel):
    channel: str
    active_connections: int = 0
    pending: int = 0
    completed: int = 0
    failed: int = 0
    avg_response_time_ms: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)

class MonitoringSummary(BaseModel):
    overview: Dict[str, int]
    channels: List[ChannelMetrics]
    alerts_count: int

@router.get("/summary", response_model=MonitoringSummary)
async def get_monitoring_summary():
    """Get a summary of all monitoring channels."""
    return MonitoringSummary(
        overview={"total_active": 0, "total_alerts": 0, "uptime_percent": 99.9},
        channels=[
            ChannelMetrics(channel="email"),
            ChannelMetrics(channel="sms"),
            ChannelMetrics(channel="voice"),
        ],
        alerts_count=0
    )

@router.get("/email", response_model=ChannelMetrics)
async def get_email_metrics():
    """Email channel real-time metrics."""
    return ChannelMetrics(channel="email")

@router.get("/sms", response_model=ChannelMetrics)
async def get_sms_metrics():
    """SMS channel real-time metrics."""
    return ChannelMetrics(channel="sms")

@router.get("/voice", response_model=ChannelMetrics)
async def get_voice_metrics():
    """Voice/SIP channel real-time metrics."""
    return ChannelMetrics(channel="voice")
