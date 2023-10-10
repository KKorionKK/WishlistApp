from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.services.parties import (
    get_party_by_id,
    create_party_,
    edit_party_,
    join_party_,
    delete_party,
)
from services.database import get_session
from services.authorization import get_current_user
from services.schemas.party_schema import PartyCreateSchema, PartySchema

party_router = APIRouter(prefix="/party", tags=["party"])


@party_router.get("/{party_uid}", response_model=PartySchema)
async def get_party(
    party_uid: str,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await get_party_by_id(
        session=session, party_uid=party_uid, user=current_user
    )


@party_router.post("/create", response_model=PartySchema)
async def create_party(
    party_info: PartyCreateSchema,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await create_party_(
        session=session, user=current_user, party_info=party_info
    )


@party_router.patch("/edit", response_model=PartySchema)
async def edit_party(
    updated_party: PartySchema,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await edit_party_(
        session=session, user=current_user, updated_party=updated_party
    )


@party_router.get("/join/{invite_code}")
async def join_party(
    invite_token: str,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await join_party_(
        session=session, user=current_user, invite_token=invite_token
    )


@party_router.delete("/delete/{party_uid}")
async def disband_party(
    party_uid: str,
    session: AsyncSession = Depends(get_session),
    current_user=Depends(get_current_user),
):
    return await delete_party(session=session, user=current_user, party_uid=party_uid)
