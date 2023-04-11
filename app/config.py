from pydantic import BaseSettings
from pydantic import BaseModel
from pydantic import Field

origins = [ "https://localhost:8082",
            "http://localhost:8082",
            "http://localhost:8005",
            "https://radhakrishnanganapathy.netlify.app"
]


API_v1 = '/name/type'

db_url = 'postgresql://postgres:ags009@localhost:5432/myproj'

# class Settings(BaseSettings):
#     db_url: str = Field(..., env='DATABASE_URL')
# settings = Settings()