from .router import create_user_router

# ルーターの生成と使用
router = create_user_router()


@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
