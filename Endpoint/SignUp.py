from fastapi import APIRouter, Depends, Body, HTTPException
from schemas import schemas
from models.SignUp import SignUp
from DataBase.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/create-user')
def user_signup(CreateUser:schemas.NewUserCreate = Body(...), db:Session=Depends(get_db)):
    check_user = SignUp.check_user(db=db, email=CreateUser.email, username=CreateUser.username)
    if check_user:
        raise HTTPException(status_code=404, detail='Username or Email already exist')
    db_return = SignUp.create_user(db=db, CreateUser=CreateUser)
    return db_return

@router.get('/login')
def login(username:str, password:str,db:Session=Depends(get_db)):
    db_return = SignUp.login(db=db, Username=username, password=password)
    if db_return:
        return ("logedin....")
    raise HTTPException(status_code=404, detail='UserNotFound')

