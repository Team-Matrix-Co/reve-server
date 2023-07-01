from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from . import utils


router = APIRouter(prefix="/auth", tags=["Users"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserAuth, db: Session = Depends(get_db)):
    db_user = models.Users(username=user.username, password=utils.encrypt_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(user: schemas.UserAuth, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.username == user.username).first()
    if not db_user or (db_user.password != utils.encrypt_password(user.password)):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    return "Logged in"
