"""Repository for Alert CRUD operations."""
from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.trunk import Alert, AlertSeverity
from app.schemas.alert import AlertCreate


class AlertRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, alert_id: int) -> Optional[Alert]:
        return self.db.query(Alert).filter(Alert.id == alert_id).first()

    def get_all(
        self,
        skip: int = 0,
        limit: int = 50,
        severity: Optional[AlertSeverity] = None,
        channel: Optional[str] = None,
        acknowledged: Optional[bool] = None,
    ) -> tuple[List[Alert], int]:
        q = self.db.query(Alert)
        if severity is not None:
            q = q.filter(Alert.severity == severity)
        if channel is not None:
            q = q.filter(Alert.channel == channel)
        if acknowledged is not None:
            q = q.filter(Alert.acknowledged == acknowledged)
        total = q.count()
        items = q.order_by(Alert.created_at.desc()).offset(skip).limit(limit).all()
        return items, total

    def create(self, data: AlertCreate) -> Alert:
        alert = Alert(**data.model_dump())
        self.db.add(alert)
        self.db.commit()
        self.db.refresh(alert)
        return alert

    def acknowledge(self, alert: Alert, by: str) -> Alert:
        alert.acknowledged = True
        alert.acknowledged_at = datetime.utcnow()
        alert.acknowledged_by = by
        self.db.commit()
        self.db.refresh(alert)
        return alert

    def delete(self, alert: Alert) -> None:
        self.db.delete(alert)
        self.db.commit()
