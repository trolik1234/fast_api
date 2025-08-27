from fastapi import APIRouter
from pydantic import BaseModel
from db.crud import create_user, get_all_user

router = APIRouter()

class UserModel(BaseModel):
    name: str
    email: str

@router.post("/reg")
async def reg(data: UserModel):
    u = await create_user(data.name, data.email)
    return {
        "name": u.name,
        "email": u.email
    }

@router.get("/users")
async def get_users():
    return await get_all_user()