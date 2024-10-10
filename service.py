from models import User
from schema import Usercreateshcema,Userdeletescheme
from sqlalchemy.orm import Session
import models
def create_user_in_db(data:Usercreateshcema,db:Session):
    new_user=User(username=data.username,password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}

def delete_user_in_db(data:Userdeletescheme,db:Session):
    user_in_db= db.query(User).filter(User.username==data.username).first()
    db.delete(user_in_db)
    db.commit()
    return {"msg":"user is deleted"}


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def update_user(db: Session, username: str, new_password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        return None
    user.password = new_password
    db.commit()
    db.refresh(user)
    return user


