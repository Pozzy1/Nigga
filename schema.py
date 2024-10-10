from pydantic import BaseModel

class Usercreateshcema(BaseModel):
    username:str
    password:str
    class Config:
        extra="forbid"

class Userdeletescheme(BaseModel):
    username:str
    class Config:
        extra="forbid"

class User(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True

class PasswordUpdate(BaseModel):
    password: str
