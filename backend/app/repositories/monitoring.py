"""Repository for ChannelMetric operations."""
from datetime import datetime, timedelta
from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.trunk import ChannelMetric


class MonitoringRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_latest(self, channel: str) -> Optional[ChannelMetric]:
        return (
            self.db.query(ChannelMetric)
            .filter(ChannelMetric.channel == channel)
            .order_by(ChannelMetric.recorded_at.desc())
            .first()
        )

    def get_latest_all_channels(self) -> List[ChannelMetric]:
        """Return the most recent snapshot for every distinct channel."""
        subq = (
            self.db.query(
                ChannelMetric.channel,
                func.max(ChannelMetric.recorded_at).label("max_ts"),
            )
            .group_by(ChannelMetric.channel)
            .subquery()
        )
        return (
            self.db.query(ChannelMetric)
            .join(
                subq,
                (ChannelMetric.channel == subq.c.channel)
                & (ChannelMetric.recorded_at == subq.c.max_ts),
            )
            .all()
        )

    def get_history(
        self,
        channel: str,
        since: Optional[datetime] = None,
        limit: int = 100,
    ) -> List[ChannelMetric]:
        q = self.db.query(ChannelMetric).filter(ChannelMetric.channel == channel)
        if since:
            q = q.filter(ChannelMetric.recorded_at >= since)
        return q.order_by(ChannelMetric.recorded_at.asc()).limit(limit).all()

    def upsert_snapshot(
        self,
        channel: str,
        active_connections: int,
        pending: int,
        completed: int,
        failed: int,
        avg_response_time_ms: float,
    ) -> ChannelMetric:
        metric = ChannelMetric(
            channel=channel,
            active_connections=active_connections,
            pending=pending,
            completed=completed,
            failed=failed,
            avg_response_time_ms=avg_response_time_ms,
        )
        self.db.add(metric)
        self.db.commit()
        self.db.refresh(metric)
        return metric
