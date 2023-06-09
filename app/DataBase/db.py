from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from ..config import settings
# import config 

DATABASE_URL = 'postgresql+psycopg2://radhakrishnan_user:PfNSlVmjWwBthsT6EsxCWC9xcyNjsbBf@dpg-cgq0nr0u9tun42uokpb0-a:5432/radhakrishnan'
engine = create_engine(DATABASE_URL)
# engine = create_engine('postgresql://postgres:ags009@localhost:5432/myproj')

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def CreateTable():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


