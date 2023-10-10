from pydantic import BaseModel


class ItemCreate(BaseModel):
    header: str
    description: str | None = None
    reference: str | None = None
    picture_path: str | None = None


class ItemSchema(ItemCreate):
    item_id: str
