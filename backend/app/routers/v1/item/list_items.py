from .router import create_item_router

# ルーターの生成と使用
router = create_item_router()


@router.get("/")
async def list_items():
    return [{"item_id": 1}, {"item_id": 2}]
