from fastapi import APIRouter

router = APIRouter(
    tags=["Health Check"]
)

@router.get(
    "/health",
    summary="Check API Status",
    description="Returns a message indicating that the Fixr Metrics API is running."
)
async def health_check() -> dict[str, str]:
    """Public health check endpoint."""

    return {
        "message": "Hello from Fixr Metrics API!"
    }