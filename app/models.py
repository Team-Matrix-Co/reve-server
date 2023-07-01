from .database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
)


class Users(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
