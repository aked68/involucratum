from app.routers.v1.router import create_factory

# ファクトリー関数の生成
create_user_router = create_factory(prefix="/users", tags=["user"])
