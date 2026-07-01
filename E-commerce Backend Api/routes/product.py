from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Product
from app.schemas import ProductCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    return {"message": "Product created"}

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
