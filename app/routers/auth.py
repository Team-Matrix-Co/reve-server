from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, oauth2
from . import utils


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.Users(
        username=user.username,
        password=utils.encrypt_password(user.password),
        name=user.name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=schemas.Token)
async def login_user(user: schemas.UserAuth, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.username == str.lower(user.username)).first()
    if not db_user or (db_user.password != utils.encrypt_password(user.password)):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    userrole = "normal"
    access_token = oauth2.create_access_token(data={"role": userrole, "login": user.username})
    return {
        "uid": db_user.uid,
        "name": db_user.name,
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=schemas.CurrentUser)
async def Current_User(current_user: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.uid == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")

    return user.name
