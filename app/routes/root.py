from fastapi import APIRouter

from app.config import app_config

router = APIRouter()


@router.get("/")
def root():
    return {
        "status": True,
        "message": app_config.app_name,
        "environment": app_config.app_env,
    }
