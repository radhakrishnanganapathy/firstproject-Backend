from sqlalchemy import Integer,String, Column, or_
from app.DataBase.db import Base
from app.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class TamilWords(Base):
    __tablename__ = 'tamil_words'
    id = Column(Integer, primary_key=True, index=True)
    words = Column(String, nullable=False, index=True)

    def addwords(db:Session, word:str):
        db_return = TamilWords(words = word)
        db.add(db_return)
        db.commit()
        db.refresh(db_return)
        return db_return
    
    def getword(db:Session):
        return db.query(TamilWords).all()
    
    def getbyletter(db:Session, letter:str):
        return db.query(TamilWords).filter(TamilWords.words.like(f'%{letter}%')).all()
    
    def getbyword(db:Session, word:str):
        return db.query(TamilWords).filter(TamilWords.words == word).first()
    
    def deleteword(db:Session, word:str):
        db_return = db.query(TamilWords).filter(TamilWords.words==word).delete()
        db.commit()
        return db_return
    
