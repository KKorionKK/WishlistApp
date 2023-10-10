from sqlalchemy.ext.asyncio import AsyncSession
from services.models import User, PartyAndUsers, Party
from services.schemas.party_schema import PartyCreateSchema, PartySchema
from services.security_utilities import get_unique_id, create_invite_token
from sqlalchemy import select, update, delete, and_
from fastapi import HTTPException, status


async def create_party_(
    session: AsyncSession, user: User, party_info: PartyCreateSchema
):
    party_uid = await get_unique_id()
    invite_token = await create_invite_token()
    party = Party(
        **party_info.model_dump(),
        owner_uid=user.user_uid,
        party_uid=party_uid,
        invite_token=invite_token
    )
    result = PartySchema.model_validate(party)
    session.add(party)
    await session.flush()
    await session.commit()
    return result


async def edit_party_(session: AsyncSession, user: User, updated_party: PartySchema):
    if user.user_uid == updated_party.owner_uid:
        await session.execute(
            update(Party)
            .where(Party.party_uid == updated_party.party_uid)
            .values(**updated_party.model_dump())
        )
        await session.flush()
        await session.commit()
        return updated_party
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to edit this party",
        )


async def is_in_party(session: AsyncSession, user: User, party_uid: str):
    user_in_party: int = await session.scalar(
        select(PartyAndUsers.id).where(
            and_(
                PartyAndUsers.party_uid == party_uid,
                PartyAndUsers.user_uid == user.user_uid,
            )
        )
    )
    if user_in_party is not None:
        return True
    else:
        return False


async def get_party_by_id(session: AsyncSession, party_uid: str, user: User):
    party = (
        await session.execute(select(Party).where(Party.party_uid == party_uid))
    ).scalar()
    if await is_in_party(
        session=session, user=user, party_uid=party_uid
    ) or await is_party_owner(session=session, user=user, party_uid=party_uid):
        rpr = PartySchema.model_validate(party)  # noqa
        return rpr
    elif party is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="First of all you need to join the party",
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Party with this id does not exist",
        )


async def increase_participants_capacity(session: AsyncSession, party_uid: str):
    party_current_capacity: int = await session.scalar(
        select(Party.participants).where(Party.party_uid == party_uid)
    )
    await session.execute(
        update(Party)
        .where(Party.party_uid == party_uid)
        .values(participants=party_current_capacity + 1)
    )
    await session.flush()
    await session.commit()
    return True


async def delete_party(session: AsyncSession, user: User, party_uid: str):
    party_owner = await session.scalar(
        select(Party.owner_uid).where(Party.party_uid == party_uid)
    )
    if user.user_uid == party_owner:
        await session.execute(delete(Party).where(Party.party_uid == party_uid))
        await session.commit()


async def is_party_owner(session: AsyncSession, user: User, party_uid: str):
    owner_uid = await session.scalar(
        select(Party.owner_uid).where(Party.party_uid == party_uid)
    )
    return owner_uid == user.user_uid


async def join_party_(session: AsyncSession, user: User, invite_token: str):
    party_uid: str = await session.scalar(
        select(Party.party_uid).where(Party.invite_token == invite_token)
    )
    if await is_party_owner(session=session, user=user, party_uid=party_uid):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Joining your own party is not permitted",
        )
    participants_row = (
        await session.execute(
            select(Party.participants, Party.max_participants).where(
                Party.party_uid == party_uid
            )
        )
    ).first()
    participants_row_map = participants_row._mapping  # noqa
    if participants_row_map.get("participants") < participants_row_map.get(
        "max_participants"
    ):
        party_and_user = PartyAndUsers(party_uid=party_uid, user_uid=user.user_uid)
        session.add(party_and_user)
        await increase_participants_capacity(session=session, party_uid=party_uid)
        await session.flush()
        await session.commit()
        return {"message": "ok"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This party has encountered a maximum participants capacity",
        )
