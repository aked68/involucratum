from .router import create_user_router

# ルーターの生成と使用
router = create_user_router()


@router.get("")
async def list_users():
    return [{"user_id": 1}, {"user_id": 2}]
