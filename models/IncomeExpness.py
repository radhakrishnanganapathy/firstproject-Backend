from sqlalchemy import Integer, String, Column, Boolean, Date, Time
from DataBase.db import Base
from schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
class IncomeExpeness(Base):
     __tablename__ = 'incomeexpness'

     id = Column(Integer, primary_key=True, index=True)
     incomeexpness = Column(Boolean, nullable=False, index=True)
     amount = Column(Integer, nullable=False, index=True)
     description = Column(String, nullable=False, index=True)
     createddate = Column(Date, nullable=False, index=True)
#     time = column(Time, nullable=False, index=True)

     def getdate(db:Session):
        try:
            return db.query(IncomeExpeness).all()
        except SQLAlchemyError as e:
            error = String(e)
            return error
        
     def create_data(db:Session,IncomeExpnessCreate:schemas.IncomeExpnessCreate):
        
          try:
               db_return = IncomeExpeness(incomeexpness=IncomeExpnessCreate.incomeexpness,amount=IncomeExpnessCreate.amount,description=IncomeExpnessCreate.incomeexpness,createddate=IncomeExpnessCreate.createddate)
               db.add(db_return)
               db.commit()
               db.refresh(db_return)
               return db_return
          except SQLAlchemyError as e:
               error = String(e)
               return(error)
            