from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = "1204"
    DB_NAME: str = "classroom_project"
    SECRET_KEY: str = "mysecretkey"

    class Config:
        env_file = ".env"

settings = Settings()
