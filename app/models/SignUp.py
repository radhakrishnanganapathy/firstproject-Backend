from sqlalchemy import Integer,String, Column, or_
from app.DataBase.db import Base
from app.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class SignUp(Base):
    __tablename__ = 'signup'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    mobile= Column(Integer, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)

    def create_user(db:Session, CreateUser: schemas.NewUserCreate):
        db_return = SignUp(username= CreateUser.username,
                           email= CreateUser.email,
                           mobile= CreateUser.mobile,
                           password = CreateUser.password)
        db.add(db_return)
        db.commit()
        db.refresh(db_return)
        return db_return
    
    def check_user(db:Session, username:str, email:str):
        db_return = db.query(SignUp).filter(or_(username == SignUp.username , email==SignUp.email)).first()
        return db_return
    
    def login(db:Session, Username:str, password:str):
        db_return = db.query(SignUp).filter(Username == SignUp.username).filter(password == SignUp.password).first()
        return db_return
    def getall(db:Session):
        db_return = db.query(SignUp).all()
        return db_return