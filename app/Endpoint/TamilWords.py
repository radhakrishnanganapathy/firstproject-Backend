from fastapi import APIRouter
from app.models.TamilWords import TamilWords
from sqlalchemy.orm import Session
from app.DataBase.db import get_db
from fastapi import Depends, Body
from app.schemas import schemas
router = APIRouter()

@router.post('/add-words')
def addword(word:str, db:Session=Depends(get_db)):
    db_return = TamilWords.addwords(db=db, word=word)
    return db_return

@router.get('/get-words')
def getword(db:Session=Depends(get_db)):
    db_return = TamilWords.getword(db=db)
    return db_return


@router.get('/get-words-by-letter')
def getletter(letter: str,db:Session=Depends(get_db)):
    db_return = TamilWords.getbyletter(db=db, letter=letter)
    return db_return