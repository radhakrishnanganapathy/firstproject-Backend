from schemas import schemas
from DataBase.db import Base
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String, Column


class RawMaterial(Base):
    __tablename__ = 'raw_material'

    id = Column(Integer, primary_key = True, index=True)
    itemname = Column(String, nullable=False, index=True)
    quantity = Column(Integer, nullable=False, index=True)
    price = Column(Integer, nullable=False, index=True)

    def add_item(AddItem :schemas.RawMaterialCreate, db:Session):
        db_return = RawMaterial(itemname = AddItem.itemname,
                                quantity = AddItem.quantity,
                                price = AddItem.price)
        db.add(db_return)
        db.commit()
        db.refresh(db_return)
        return db_return
    
    def get_item(db:Session):
        db_return = db.query(RawMaterial).all()
        return db_return
    
    def delete_item(id: int , db:Session):
        db_return = db.query(RawMaterial).filter(id == RawMaterial.id).delete()
        db.commit()
        return db_return