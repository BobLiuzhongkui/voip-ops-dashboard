# com-management-backend
├── frontend/              # Next.js + TypeScript + Tailwind + shadcn/ui
│   ├── src/app/           # App Router pages
│   ├── src/components/ui  # shadcn/ui base components
│   ├── src/stores/        # Zustand state stores
│   ├── src/services/      # API service layer
│   └── src/types/         # TypeScript type definitions
└── backend/               # FastAPI + Pydantic + Service/Repository
    └── app/
        ├── api/v1/        # API routes
        ├── core/          # Config, DB, security
        ├── models/        # SQLAlchemy models
        ├── schemas/       # Pydantic schemas
        ├── services/      # Business logic layer
        ├── repositories/  # Data access layer
        └── adapters/      # External service adapters

# voip-ops-dashboard
├── frontend/              # Next.js + TypeScript + Tailwind + shadcn/ui
│   ├── src/app/           # App Router pages (monitoring, alerts, reports, trunks, agents)
│   ├── src/components/    # Dashboard, charts, monitoring widgets
│   └── src/stores/        # Zustand real-time state
└── backend/               # FastAPI + Celery workers
    └── app/
        ├── api/v1/        # API routes (monitoring, alerts, trunks, reports)
        ├── adapters/      # VoIP provider adapters (SIP, Twilio, etc.)
        └── workers/       # Celery background task workers
