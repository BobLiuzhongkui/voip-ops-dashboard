from sqlalchemy.orm import DeclarativeBase
from enum import Enum

class Base(DeclarativeBase):
    pass

class MetricType(str, Enum):
    CALLS = "calls"
    SMS = "sms"
    EMAIL = "email"

class AlertSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
