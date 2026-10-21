from fastapi import APIRouter

user_routes = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@user_routes.get("/")
def get_users():
    return {"data": []}


@user_routes.get("/{user_id}")
def get_user(user_id: int):
    return {
        "data": {
            "user_id": user_id,
        }
    }
