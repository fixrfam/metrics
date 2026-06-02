from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import (
    check_database_connection,
    get_db,
)

router = APIRouter(
    tags=["Health Check"]
)


@router.get(
    "/health",
    summary="Check API Health",
    description="Returns the current health status of the API and its dependencies.",
)
async def health_check(
    db: Session = Depends(get_db),
) -> dict:
    """Checks API and database availability."""

    database_status = (
        "healthy"
        if check_database_connection(db)
        else "unhealthy"
    )

    return {
        "status": (
            "healthy"
            if database_status == "healthy"
            else "degraded"
        ),
        "service": "fixr-metrics-api",
        "version": "1.0.0",
        "timestamp": datetime.now(
            ZoneInfo("America/Sao_Paulo")
        ).isoformat(),
        "dependencies": {
            "database": database_status,
        },
    }