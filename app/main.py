from fastapi import FastAPI
from app.DataBase import db
from app.Api.api import api_router
from app import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

db.CreateTable()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {'I am':'alive'}


app.include_router(api_router, prefix=config.API_v1)