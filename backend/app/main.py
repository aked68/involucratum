from fastapi import FastAPI

from .routers import v1

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


# v1をすべて登録
# app.include_router(v1.router)

# APIグループ指定で登録
# app.include_router(v1.item.router)
# app.include_router(v1.user.router)

# エンドポイント指定で登録
app.include_router(v1.item.list_items.router)
app.include_router(v1.user.list_users.router)
