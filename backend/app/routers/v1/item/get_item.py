from .router import create_item_router

# ルーターの生成と使用
router = create_item_router()


@router.get("/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
