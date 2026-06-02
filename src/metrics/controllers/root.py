from fastapi import APIRouter

router = APIRouter(
    tags=["Root"]
)

@router.get(
    "/",
    summary="API root",
    description="Welcome message with a link to the documentation.",
)
async def root() -> dict[str, str]:
    """Public API root endpoint."""

    return {
        "message": "Hello from Fixr Metrics API! Reach the documentation at /docs"
    }
