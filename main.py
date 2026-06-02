from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from src.metrics.controllers.health import router as health_router
from src.metrics.controllers.root import router as root_router

app = FastAPI(
    title="Fixr Metrics API",
    description=(
        "Centralized API for managing metrics, KPIs and chart data "
        "across all organizations using Fixr."
    ),
    version="1.0.0",
)

app.include_router(root_router)
app.include_router(health_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )