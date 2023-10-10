from services.schemas.user_schema import UserRegisterSchema, UserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy import select
from datetime import timedelta, datetime
from services.models import User
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from services.config import SecuritySettings
from typing import Annotated
from services.database import get_session
from api_v1.services.users import get_user
from services.zodiac_selector import get_zodiac
from services.security_utilities import get_unique_id

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/v1/authorization/token")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_pasword: str):
    return pwd_context.verify(plain_password, hashed_pasword)


async def get_user(session: AsyncSession, email: str):
    user = (await session.execute(select(User).where(User.email == email))).scalar()
    if user:
        return UserSchema(
            user_uid=user.user_uid,
            email=user.email,
            name=user.name,
            nickname=user.nickname,
            password=user.password,
            gender=user.gender,
            zodiac=user.zodiac,
            birthday=user.birthday,
        )
    else:
        return None


async def authenticate_user(session: AsyncSession, email: str, password: str):
    user = await get_user(session=session, email=email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=SecuritySettings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SecuritySettings.SECRET, algorithm=SecuritySettings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_schema)], session=Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, SecuritySettings.SECRET, algorithms=[SecuritySettings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(session=session, email=username)
    if user is None:
        raise credentials_exception
    return user


async def get_login_access_token(form_data, session=Depends(get_session)):
    user = await authenticate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=SecuritySettings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def register_user(user_data: UserRegisterSchema, session: AsyncSession):
    uid = await get_unique_id()
    user_dict = user_data.model_dump()
    if await get_user(session=session, email=user_dict.get("email")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account with this email is already created",
        )
    user_dict["password"] = get_password_hash(user_dict["password"])
    zodiac = get_zodiac(user_dict.get("birthday"))
    if user_dict.get("gender") not in ["М", "Ж"]:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="There is only two genders"
        )
    user = User(**user_dict, user_uid=uid, zodiac=zodiac)
    session.add(user)
    await session.flush()
    await session.commit()

    access_token_expires = timedelta(
        minutes=SecuritySettings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user_data.model_dump().get("email")},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
