from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.authorization import (
    get_login_access_token,
    register_user,
)
from services.database import get_session
from typing import Annotated
from services.schemas.user_schema import UserRegisterSchema
from fastapi.security import OAuth2PasswordRequestForm
from services.schemas.security import Token

authorization_router = APIRouter(
    tags=["authorization"],
    prefix="/authorization",
)


@authorization_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(get_session),
):
    return await get_login_access_token(form_data=form_data, session=session)


@authorization_router.post("/register", response_model=Token)
async def register(
    user_data: UserRegisterSchema, session: AsyncSession = Depends(get_session)
):
    return await register_user(user_data=user_data, session=session)
