from api_v1.routes.authorization import authorization_router
from api_v1.routes.user import user_router
from api_v1.routes.item import item_router
from api_v1.routes.profile import profile_router
from api_v1.routes.party import party_router
from api_v1.routes.chat import chat_route
from fastapi import APIRouter

api_router = APIRouter(prefix="/v1")
api_router.include_router(authorization_router)
api_router.include_router(user_router)
api_router.include_router(item_router)
api_router.include_router(profile_router)
api_router.include_router(party_router)
api_router.include_router(chat_route)
