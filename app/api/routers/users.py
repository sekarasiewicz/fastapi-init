from fastapi import APIRouter

router = APIRouter()


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
