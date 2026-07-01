from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Order
from app.schemas import OrderCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict(), user_id=1)
    db.add(db_order)
    db.commit()
    return {"message": "Order placed"}
