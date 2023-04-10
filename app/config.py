from pydantic import BaseSettings
from pydantic import BaseModel
from pydantic import Field

origins = [ "https://localhost:8080",
            "http://localhost:8080",
            "http://localhost:8005",
]


API_v1 = '/name/type'

# dbUrl = 'postgresql://postgres:ags009@localhost:5432/myproj'

class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')
settings = Settings()