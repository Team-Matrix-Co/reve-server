import csv
import codecs
from fastapi import APIRouter, status, Depends, File, UploadFile
from sqlalchemy.orm import Session
from datetime import datetime
from ..database import get_db
from .. import models


router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(
    userid: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, "utf-8"))
    data = {}
    for index, rows in enumerate(csvReader):
        print(rows)
        db_item = models.Items(
            created_at=datetime.now(),
            order_date=datetime.strptime(rows["date"], "%m/%d/%Y"),
            uid=userid,
            name=rows["item"],
            price=rows["price"],
            cost=rows["cost"],
            inventory=rows["quantity"],
            order=rows["order"],
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        data[index] = rows
    file.file.close()
    return data
