from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from services.models import User
from services.schemas.user_schema import UserSchema, UserRegisterSchema
from fastapi import status, HTTPException
from services.zodiac_selector import get_zodiac


async def get_user(session: AsyncSession, nickname: str):
    user = await session.execute(select(User).where(User.nickname == nickname))
    if user:
        user_result = user.scalar()
        return UserSchema.model_validate(user_result)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
        )


async def edit_user(
    session: AsyncSession, current_user: User, updated_user: UserRegisterSchema
):
    if current_user.birthday != updated_user.birthday:
        current_user.birthday = get_zodiac(updated_user.birthday)
    await session.execute(
        update(User)
        .where(User.user_uid == current_user.user_uid)
        .values(**updated_user.model_dump())
    )
    await session.commit()
    return {"message": "ok"}
