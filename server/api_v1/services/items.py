from sqlalchemy import select, and_, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from services.models import User, Item, UserAndItems
from services.schemas.item_schema import ItemCreate, ItemSchema
from fastapi import HTTPException, status
from services.security_utilities import get_unique_id


async def create_item_by_user(
    user: User, session: AsyncSession, item_schema: ItemCreate
):
    item_id = await get_unique_id()
    item = Item(**item_schema.model_dump(), item_id=item_id)
    session.add(item)
    await session.flush()
    uai = UserAndItems(user_uid=user.user_uid, item_id=item_id)
    session.add(uai)
    await session.flush()
    await session.commit()
    return ItemSchema(**item_schema.model_dump(), item_id=item_id)


async def get_all_items(user: User, session: AsyncSession) -> list[ItemSchema]:
    all_items = (
        await session.execute(
            select(
                Item.item_id,
                Item.header,
                Item.reference,
                Item.description,
                Item.picture_path,
            )
            .join(UserAndItems, UserAndItems.item_id == Item.item_id)
            .where(UserAndItems.user_uid == user.user_uid)
        )
    ).all()
    items = list()
    for i in all_items:
        items.append(ItemSchema(**i._mapping))
    return items


async def get_item_by_id(item_id: str, session: AsyncSession) -> Item:
    item_row = (
        await session.execute(select(Item).where(Item.item_id == item_id))
    ).first()
    if item_row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    item_mapping = item_row._mapping  # noqa
    item = Item(**item_mapping)
    return item


async def edit_item_by_id(user: User, session: AsyncSession, updated_item: ItemSchema):
    item = await get_item_by_id(item_id=updated_item.item_id, session=session)
    is_owner = await check_owner(item, session, user)
    if is_owner:
        await session.execute(
            update(Item)
            .where(Item.item_id == updated_item.item_id)
            .values(**updated_item.model_dump())
        )
        await session.commit()
        return {"message": "ok"}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized to edit this item",
    )


async def check_owner(item: Item, session: AsyncSession, user: User):
    return await session.scalar(
        select(UserAndItems).where(
            and_(
                UserAndItems.user_uid == user.user_uid,
                UserAndItems.item_id == item.item_id,
            )
        )
    )


async def delete_item_by_id(user: User, session: AsyncSession, item_id: str):
    item = await get_item_by_id(item_id=item_id, session=session)
    if await check_owner(item=item, session=session, user=user):
        await session.execute(delete(Item).where(Item.item_id == item_id))
        await session.execute(
            delete(UserAndItems).where(UserAndItems.item_id == item_id)
        )
        await session.commit()
        return {"message": "ok"}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized to edit this item",
    )
