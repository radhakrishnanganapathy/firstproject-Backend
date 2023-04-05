from fastapi import APIRouter, HTTPException, Depends, Body
from schemas import schemas
from models.RawMaterial import RawMaterial
from DataBase.db import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post('/add-item')
def add_item(AddItem: schemas.RawMaterialCreate = Body(...), db:Session = Depends(get_db)):
    db_return = RawMaterial.add_item(db=db, AddItem=AddItem)
    return db_return

@router.get('/get-item')
def get_item(db: Session = Depends(get_db)):
    db_return = RawMaterial.get_item(db=db)
    return db_return

@router.delete('/delete-item')
def delete_item(id:int , db: Session = Depends(get_db)):
    db_return = RawMaterial.delete_item(db=db, id=id)
    return db_return