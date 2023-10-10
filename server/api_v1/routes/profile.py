from fastapi import APIRouter
from api_v1.services.users import get_user, edit_user
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.database import get_session
from services.schemas.user_schema import UserSchema, UserRegisterSchema
from services.models import User
from services.authorization import get_current_user

profile_router = APIRouter(tags=["profile"], prefix="/profile")


@profile_router.get("/", response_model=UserSchema)
async def get_user_self(
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Получение данных о текущем пользователе"""
    return await get_user(nickname=current_user.nickname, session=session)


@profile_router.post("/edit")
async def edit_profile_self(
    updated_user: UserRegisterSchema,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Редактирование данных пользователя"""
    return await edit_user(
        session=session, current_user=current_user, updated_user=updated_user
    )
