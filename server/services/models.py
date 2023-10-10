from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Boolean, Column, DateTime

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    item_id = Column(String, primary_key=True)
    header = Column(String, nullable=False)
    description = Column(String, nullable=True)
    reference = Column(String, nullable=True)
    picture_path = Column(String, nullable=True)


class User(Base):
    __tablename__ = "users"
    user_uid = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    birthday = Column(DateTime(timezone=True), nullable=True)
    zodiac = Column(String, nullable=True)


class UserAndItems(Base):
    __tablename__ = "user_and_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(String, nullable=False)
    user_uid = Column(String, nullable=False)


class Party(Base):
    __tablename__ = "parties"
    party_uid = Column(String, primary_key=True)
    owner_uid = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    invite_token = Column(String, nullable=False, unique=True)
    max_participants = Column(Integer, nullable=False)
    participants = Column(Integer, nullable=False, default=0)


class PartyAndUsers(Base):
    __tablename__ = "party_and_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    party_uid = Column(String, nullable=False)
    user_uid = Column(String, nullable=False)


class Chat(Base):
    __tablename__ = "chats"
    chat_uid = Column(String, primary_key=True)
    party_uid = Column(String, nullable=False)
    history = Column()


class MigrationVersion(Base):
    __tablename__ = "migrtaion_version"
    id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False)
