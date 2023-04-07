from pydantic import BaseModel , EmailStr, SecretStr
from datetime import date

class NewUserCreate(BaseModel):
    username: str
    email: EmailStr
    mobile: int
    password: str

    class Config:
        orm_mode = True

class UserLogIn(BaseModel):
    username: str
    password: SecretStr

    class Config:
        orm_mode = True


class IncomeExpnessCreate(BaseModel):
    incomeexpness : bool
    amount : int
    description : str
    createddate : date
#     time: Time

    class Config:
        orm_mode = True

class IncomeExpnessRead(IncomeExpnessCreate):
    id: int

class RawMaterialCreate(BaseModel):
    itemname : str
    quantity: str
    price : int

    class Config:
        orm_mode = True

class RawMaterialRead(RawMaterialCreate):
    id : int
