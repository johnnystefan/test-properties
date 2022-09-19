# Pydantic
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = '3.130.126.210'
    database_port: str = 3309
    database_username: str = 'pruebas'
    database_password: str = 'VGbt3Day5R'
    database_name: str = 'habi_db'

    class Config:
        env_file = ".env"


settings = Settings()
