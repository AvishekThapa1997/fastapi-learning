from fastapi import APIRouter, FastAPI

# from app import app_config It is because of __init__.py same like index.js file
from app.config import app_config
from app.routes.root import router
from app.routes.users import user_routes

app = FastAPI(
    title=app_config.app_name,
)

api_routes = APIRouter(
    prefix="/api",
)

api_routes.include_router(router)
api_routes.include_router(user_routes)

app.include_router(api_routes)
app.include_router(user_routes)
