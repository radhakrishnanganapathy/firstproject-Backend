from fastapi import APIRouter


from Endpoint import IncomeExpness
from Endpoint import SignUp
from Endpoint import RawMaterial

api_router = APIRouter()

api_router.include_router(IncomeExpness.router, prefix='/income', tags=["IncomeExpness"])
api_router.include_router(SignUp.router, prefix='/signup', tags=['Signups'])
api_router.include_router(RawMaterial.router, prefix='/item', tags=['Raw Material'])