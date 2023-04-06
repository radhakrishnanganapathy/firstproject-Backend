from fastapi import FastAPI
from DataBase import db
from Api import api
import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

db.CreateTable()

app.include_router(api.api_router, prefix=config.API_v1)