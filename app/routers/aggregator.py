from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/data", tags=["Data Aggregator"])


@router.post("")
async def fetch(
    userid: int,
    db: Session = Depends(get_db),
):
    data = {}
    db_items = db.query(models.Items).filter(models.Items.uid == userid).all()
    for index, item in enumerate(db_items):
        data[index] = item
    return data
