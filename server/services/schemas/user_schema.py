from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserRegisterSchema(BaseModel):
    email: str
    name: str
    nickname: str
    password: str
    gender: str
    birthday: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "mactep@cekca.ru",
                "name": "Zaur",
                "nickname": "KKorionKK",
                "password": "123",
                "gender": "М",
                "birthday": "2003-03-14T13:19:09.309Z",
            }
        }
    }


class UserSchema(UserRegisterSchema):
    model_config = ConfigDict(from_attributes=True)
    user_uid: str
    zodiac: str
