import openai
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..config import settings
from .. import models

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

openai.api_key = settings.api_key


@router.post("")
async def general_recommendation(
    userid: int,
    db: Session = Depends(get_db),
):
    shop_items = {}
    db_items = db.query(models.Items).filter(models.Items.uid == userid).all()
    for index, item in enumerate(db_items):
        total = item.price * item.order - item.cost * item.inventory
        name = str.lower(item.name)
        if name not in shop_items:
            shop_items[name] = total
        else:
            shop_items[name] += total

    # Define the system message
    system_msg = (
        "You are a helpful assistant who understands businesses and you are Filipino bussiness data analyst and you are"
        + "going to help the small business owner to make a decision using simple language, and straightforward short"
        + "answer. You don't ask further questions and will answer based on given data. You will speak in Tagalog."
    )

    # Define the user message
    user_msg = (
        "Hi, I am a small business owner and I am looking for some recommendations on what to do next. I have a small "
        + f"shop and I sell {', '.join(shop_items.keys())} with the following profits/loss, "
        + f"{', '.join([str(item) for item in shop_items.values()])} ."
    )

    # Create a dataset using GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )

    return response["choices"][0]["message"]["content"]
