from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserAuth(User):
    password: str


class UserDetail(User):
    uid: int
    user_type: str

    class Config:
        orm_mode = True
