"""
VoIP Operations Dashboard Backend - FastAPI entry point.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router as v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("📡 VoIP Operations Dashboard starting...")
    yield
    print("👋 VoIP Operations Dashboard shutting down...")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url=f"{settings.API_V1_PREFIX}/docs",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(o) for o in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_router, prefix=settings.API_V1_PREFIX)

    @app.get("/health")
    def health_check():
        return {"status": "ok", "service": "voip-ops-dashboard"}

    return app


app = create_app()
