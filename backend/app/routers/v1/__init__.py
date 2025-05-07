from fastapi import APIRouter

from . import item, user

router = APIRouter()
router.include_router(user.router)
router.include_router(item.router)

__all__ = ["router"]
