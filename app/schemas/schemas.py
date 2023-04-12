from pydantic import BaseModel , EmailStr, SecretStr
from datetime import date

class NewUserCreate(BaseModel):
    username: str
    email: str
    mobile: int
    password: str

    class Config:
        orm_mode = True

class UserLogIn(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class ProductionCreate(BaseModel):
    item : str
    quantity: int
    amount : int
    createddate : date
#     time: Time

    class Config:
        orm_mode = True

class ProductionRead(ProductionCreate):
    id: int

class SalesCreate(BaseModel):
    item : str
    customer: str
    quantity: int
    amount : int
    createddate : date
#     time: Time

    class Config:
        orm_mode = True

class SalesRead(SalesCreate):
    id: int

class SalaryCreate(BaseModel):
    worker : str
    salary: int
    createddate : date
#     time: Time

    class Config:
        orm_mode = True

class SalaryRead(SalaryCreate):
    id: int

class RawMaterialCreate(BaseModel):
    itemname : str
    quantity: str
    price : int

    class Config:
        orm_mode = True

class RawMaterialRead(RawMaterialCreate):
    id : int
