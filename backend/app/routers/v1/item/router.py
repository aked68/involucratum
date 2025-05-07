from app.routers.v1.router import create_factory

# ファクトリー関数の生成
create_item_router = create_factory(
    prefix="/items",
    tags=["item"],
    responses={500: {"description": "Internal Server Error"}},
)
