from fastapi import APIRouter
from app.models.Salary import Salary
from sqlalchemy.orm import Session
from app.DataBase.db import get_db
from fastapi import Depends, Body
from app.schemas import schemas
router = APIRouter()

@router.get('/home')
def get_data(db:Session=Depends(get_db)):
    db_return = Salary.getdate(db)
    return db_return

@router.post('/create')
def create_date(SalaryCreate: schemas.SalaryCreate = Body(...), db:Session=Depends(get_db)):
    db_return = Salary.create_data(db=db, SalaryCreate=SalaryCreate)
    return db_return