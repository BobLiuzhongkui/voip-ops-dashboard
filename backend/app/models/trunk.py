"""SQLAlchemy models for the VoIP Operations Dashboard."""
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    Boolean, Column, DateTime, Enum, Float, Integer,
    String, Text, func,
)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# ──────────────────────────────────────────────
# Enums
# ──────────────────────────────────────────────

class MetricType(str, PyEnum):
    CALLS = "calls"
    SMS = "sms"
    EMAIL = "email"


class AlertSeverity(str, PyEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class TrunkStatus(str, PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DEGRADED = "degraded"


# ──────────────────────────────────────────────
# ORM Models
# ──────────────────────────────────────────────

class Trunk(Base):
    """SIP trunk / provider configuration."""
    __tablename__ = "trunks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    provider = Column(String(100), nullable=False)
    sip_uri = Column(String(255), nullable=False)
    username = Column(String(100), nullable=True)
    status = Column(Enum(TrunkStatus), default=TrunkStatus.INACTIVE, nullable=False)
    channels_max = Column(Integer, default=30, nullable=False)
    channels_active = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class Alert(Base):
    """Operational alert record."""
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    severity = Column(Enum(AlertSeverity), nullable=False, index=True)
    channel = Column(String(50), nullable=False, index=True)  # email | sms | voice
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    acknowledged = Column(Boolean, default=False, nullable=False)
    acknowledged_at = Column(DateTime, nullable=True)
    acknowledged_by = Column(String(100), nullable=True)


class ChannelMetric(Base):
    """Point-in-time snapshot of a communication channel."""
    __tablename__ = "channel_metrics"

    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String(50), nullable=False, index=True)
    active_connections = Column(Integer, default=0, nullable=False)
    pending = Column(Integer, default=0, nullable=False)
    completed = Column(Integer, default=0, nullable=False)
    failed = Column(Integer, default=0, nullable=False)
    avg_response_time_ms = Column(Float, default=0.0, nullable=False)
    recorded_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)


class User(Base):
    """Dashboard operator account."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
