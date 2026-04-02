"""API v1 router aggregation."""
from fastapi import APIRouter
from app.api.v1.endpoints.monitoring.monitoring import router as monitoring_router
from app.api.v1.endpoints.alerts.alerts import router as alerts_router
from app.api.v1.endpoints.trunks.trunks import router as trunks_router
from app.api.v1.endpoints.reports.reports import router as reports_router

api_router = APIRouter()
api_router.include_router(monitoring_router, prefix="/monitoring", tags=["monitoring"])
api_router.include_router(alerts_router, prefix="/alerts", tags=["alerts"])
api_router.include_router(trunks_router, prefix="/trunks", tags=["trunks"])
api_router.include_router(reports_router, prefix="/reports", tags=["reports"])
