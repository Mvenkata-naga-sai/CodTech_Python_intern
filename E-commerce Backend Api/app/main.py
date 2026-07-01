from fastapi import FastAPI
from app.db import Base, engine
from app.routes import user, product, order

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/auth")
app.include_router(product.router, prefix="/products")
app.include_router(order.router, prefix="/orders")

@app.get("/")
def root():
    return {"message": "E-Commerce API Running"}
