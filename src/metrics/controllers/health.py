from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    """Public health check endpoint."""

    return {
        "message": "Hello from Fixr Metrics API!"
    }