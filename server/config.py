from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    TRAVILY_API_KEY: str  # ← no default!

    class Config:
        env_file = ".env"
