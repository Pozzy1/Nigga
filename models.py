from sqlalchemy import Column,Integer,String
from db import Base,engine

#comment
class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)

class User2(Base):
    __tablename__="user2"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)



Base.metadata.create_all(bind=engine)
