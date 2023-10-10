from fastapi import APIRouter
from api_v1.services.users import get_user
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.database import get_session
from services.schemas.user_schema import UserSchema

user_router = APIRouter(tags=["user"], prefix="/user")


@user_router.get("/{nickname}", response_model=UserSchema)
async def get_user_by_nickname(
    nickname: str, session: AsyncSession = Depends(get_session)
):
    """Получение данных о пользователе"""
    return await get_user(nickname=nickname, session=session)
