from sqlalchemy import Integer, String, Column, Boolean, Date, Time
from app.DataBase.db import Base
from app.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
class Salary(Base):
     __tablename__ = 'salary'

     id = Column(Integer, primary_key=True, index=True)
     worker = Column(String, nullable=False, index=True)
     salary = Column(Integer, nullable=False, index=True)
     createddate = Column(Date, nullable=False, index=True)
#     time = column(Time, nullable=False, index=True)

     def getdate(db:Session):
        try:
            return db.query(Salary).all()
        except SQLAlchemyError as e:
            error = String(e)
            return error
        
     def create_data(db:Session,SalaryCreate:schemas.SalaryCreate):
        
          try:
               db_return = Salary(worker=SalaryCreate.worker,
                                  salary=SalaryCreate.salary,
                                  createddate=SalaryCreate.createddate)
               db.add(db_return)
               db.commit()
               db.refresh(db_return)
               return db_return
          except SQLAlchemyError as e:
               error = String(e)
               return(error)
            