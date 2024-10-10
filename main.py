from fastapi import FastAPI,Depends,HTTPException
from db import get_db
from sqlalchemy.orm import Session
from schema import Usercreateshcema,Userdeletescheme
from service import create_user_in_db,delete_user_in_db
import schema
import service


app = FastAPI()


@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}

@app.post("/user")
def create_user(item: Usercreateshcema,db:Session=Depends(get_db)):
    message=create_user_in_db(data=item,db=db)
    return message

@app.delete("/user")
def delete_user(item:Userdeletescheme,db:Session=Depends(get_db)):
    message=delete_user_in_db(data=item,db=db)
    return message

@app.get("/user/{username}", response_model=schema.User)
def get_user(username: str, db: Session = Depends(get_db)):
    user = service.get_user(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/{username}", response_model=schema.User)
def update_user(username: str, password_update: schema.PasswordUpdate, db: Session = Depends(get_db)):
    user = service.update_user(db, username, password_update.password)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
