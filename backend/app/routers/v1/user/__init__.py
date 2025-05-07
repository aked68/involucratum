from fastapi import APIRouter

from . import get_user, list_users

router = APIRouter()
router.include_router(list_users.router)
router.include_router(get_user.router)

__all__ = ["router"]
