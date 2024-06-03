from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:secret@localhost/bambuz"

    class Config:
        env_file = ".env"


settings = Settings()
