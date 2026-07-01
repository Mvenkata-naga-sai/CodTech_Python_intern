from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User
from app.schemas import UserCreate
from app.auth import hash_password, create_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    token = create_token({"sub": user.email})
    return {"access_token": token}
