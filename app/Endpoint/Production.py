from fastapi import APIRouter
from app.models.Production import Production
from sqlalchemy.orm import Session
from app.DataBase.db import get_db
from fastapi import Depends, Body
from app.schemas import schemas
router = APIRouter()

@router.get('/home')
def get_data(db:Session=Depends(get_db)):
    db_return = Production.getdate(db)
    return db_return

@router.post('/create')
def create_date(ProductionCreate: schemas.ProductionCreate = Body(...), db:Session=Depends(get_db)):
    db_return = Production.create_data(db=db, ProductionCreate=ProductionCreate)
    return db_return