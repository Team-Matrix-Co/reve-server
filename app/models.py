from .database import Base
from sqlalchemy import Column, Integer, String, Date


class Users(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    user_type = Column(String, default="normal")
    name = Column(String)


class Stores(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Items(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    created_at = Column(Date)
    order_date = Column(Date)
    name = Column(String)
    price = Column(Integer)
    cost = Column(Integer)
    inventory = Column(Integer)
    order = Column(Integer)
