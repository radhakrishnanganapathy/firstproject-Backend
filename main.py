from fastapi import FastAPI
from DataBase import db
from Endpoint import IncomeExpness
from Api import api
import config
app = FastAPI()

@app.get('/')
def index():
    return {'I am':'alive'}

db.CreateTable()

app.include_router(api.api_router, prefix=config.API_v1)