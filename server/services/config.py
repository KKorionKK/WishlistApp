from dotenv import dotenv_values, find_dotenv
from dataclasses import dataclass


@dataclass
class Settings:
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_URL: str
    DATABASE_PORT: str
    DATABASE_DBMS: str


@dataclass
class SecuritySettings:
    SECRET = "eab24ce076113356276314449db7594ce8e46d610afa06ec5d2b3c206c2a9fd1"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class SettingsDotEnv:
    def get_settings(self) -> Settings:
        sett = dotenv_values(find_dotenv())
        return Settings(**sett)
