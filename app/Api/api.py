from fastapi import APIRouter


from app.Endpoint import Production
from app.Endpoint import SignUp
from app.Endpoint import RawMaterial
from app.Endpoint import Sales
from app.Endpoint import Salary
from app.Endpoint import PDFDownloader


api_router = APIRouter()

api_router.include_router(Production.router, prefix='/production', tags=["Production"])
api_router.include_router(SignUp.router, prefix='/signup', tags=['Signups'])
api_router.include_router(RawMaterial.router, prefix='/item', tags=['Raw Material'])
api_router.include_router(Sales.router, prefix='/sales', tags=['sales'])
api_router.include_router(Salary.router, prefix='/salary', tags=['Salary'])
api_router.include_router(PDFDownloader.router, prefix='/pdfdownloader', tags=['PDFDownloader'])