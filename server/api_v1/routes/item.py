from fastapi import APIRouter, Depends
from services.authorization import get_current_user
from services.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.services.items import (
    get_all_items,
    create_item_by_user,
    edit_item_by_id,
    delete_item_by_id,
)
from services.schemas.item_schema import ItemCreate, ItemSchema

item_router = APIRouter(tags=["Items"], prefix="/items")


@item_router.get("/")
async def get_all_my_items(
    session: AsyncSession = Depends(get_session), current_user=Depends(get_current_user)
):
    return await get_all_items(user=current_user, session=session)


@item_router.post("/create", response_model=ItemSchema)
async def create_item(
    item: ItemCreate,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await create_item_by_user(
        item_schema=item, session=session, user=current_user
    )


@item_router.post("/edit")
async def edit_item(
    item: ItemSchema,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await edit_item_by_id(updated_item=item, session=session, user=current_user)


@item_router.delete("/delete/{item_id}")
async def delete_item(
    item_id: str,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await delete_item_by_id(user=current_user, session=session, item_id=item_id)
