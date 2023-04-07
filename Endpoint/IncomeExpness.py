from fastapi import APIRouter
from models.IncomeExpness import IncomeExpeness
from sqlalchemy.orm import Session
from DataBase.db import get_db
from fastapi import Depends, Body
from schemas import schemas
router = APIRouter()

@router.get('/home')
def get_data(db:Session=Depends(get_db)):
    db_return = IncomeExpeness.getdate(db)
    return db_return

@router.post('/create')
def create_date(IncomeExpenssCreate: schemas.IncomeExpnessCreate = Body(...), db:Session=Depends(get_db)):
    db_return = IncomeExpeness.create_data(db=db, IncomeExpnessCreate=IncomeExpenssCreate)
    return db_return