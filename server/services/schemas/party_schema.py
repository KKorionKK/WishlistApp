from pydantic import BaseModel, ConfigDict


class PartyCreateSchema(BaseModel):
    name: str
    description: str
    max_participants: int
    participants: int = 0
    model_config = ConfigDict(from_attributes=True)


class PartySchema(PartyCreateSchema):
    model_config = ConfigDict(from_attributes=True)
    invite_token: str
    party_uid: str
    owner_uid: str
