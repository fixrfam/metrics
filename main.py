from dotenv import load_dotenv
from fastapi import FastAPI

from src.metrics.controllers.health import router as health_router

load_dotenv()

app = FastAPI(
    title="Fixr Metrics API",
)

app.include_router(health_router)