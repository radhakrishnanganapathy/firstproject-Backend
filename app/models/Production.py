from sqlalchemy import Integer, String, Column, Boolean, Date, Time
from app.DataBase.db import Base
from app.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
class Production(Base):
     __tablename__ = 'production'

     id = Column(Integer, primary_key=True, index=True)
     item = Column(String, nullable=False, index=True)
     quantity = Column(String, nullable=False, index=True)
     amount = Column(Integer, nullable=False, index=True)
     createddate = Column(Date, nullable=False, index=True)
#     time = column(Time, nullable=False, index=True)

     def getdate(db:Session):
        try:
            return db.query(Production).all()
        except SQLAlchemyError as e:
            error = String(e)
            return error
        
     def create_data(db:Session,ProductionCreate:schemas.ProductionCreate):
        
          try:
               db_return = Production(item=ProductionCreate.item,amount=ProductionCreate.amount,quantity=ProductionCreate.quantity,createddate=ProductionCreate.createddate)
               db.add(db_return)
               db.commit()
               db.refresh(db_return)
               return db_return
          except SQLAlchemyError as e:
               error = String(e)
               return(error)
            