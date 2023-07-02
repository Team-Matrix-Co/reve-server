from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str


class UserAuth(User):
    password: str


class UserCreate(UserAuth):
    name: str


class UserDetail(UserCreate):
    uid: int
    user_type: str

    class Config:
        orm_mode = True


class CurrentUser(BaseModel):
    uid: int


class Fetch(BaseModel):
    uid: int


class FetchDate(Fetch):
    date = str


class Token(BaseModel):
    uid: int
    name: str
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    login: Optional[str] = None


class Store(BaseModel):
    store_id: int
    name: str


class StoreDetail(Store):
    category: str
    description: str
    location: str


class Item(BaseModel):
    uid: int
    item_id: int
    name: str

    class Config:
        orm_mode = True


class ItemDetail(Item):
    price: int
    cost: int
    inventory: int

    class Config:
        orm_mode = True
