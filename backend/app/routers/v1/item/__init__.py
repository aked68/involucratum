from fastapi import APIRouter

from . import get_item, list_items

router = APIRouter()
router.include_router(list_items.router)
router.include_router(get_item.router)

__all__ = ["router"]
