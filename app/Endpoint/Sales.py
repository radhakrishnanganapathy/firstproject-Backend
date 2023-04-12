from fastapi import APIRouter
from app.models.Sales import Sales
from sqlalchemy.orm import Session
from app.DataBase.db import get_db
from fastapi import Depends, Body
from app.schemas import schemas
router = APIRouter()

@router.get('/home')
def get_data(db:Session=Depends(get_db)):
    db_return = Sales.getdate(db)
    return db_return

@router.post('/create')
def create_date(SalesCreate: schemas.SalesCreate = Body(...), db:Session=Depends(get_db)):
    db_return = Sales.create_data(db=db, SalesCreate=SalesCreate)
    return db_return