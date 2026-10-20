from fastapi import FastAPI

from config import app_config

app = FastAPI(
    title=app_config.app_name,
)


@app.get("/")
def root():
    return {
        "message": app_config.app_name,
        "environment": app_config.app_env,
    }
