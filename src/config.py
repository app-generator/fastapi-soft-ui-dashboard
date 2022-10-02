from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = 'test'
    database_port: int = 0
    database_password: str = 'test'
    database_name: str = 'test'
    database_username: str = 'test'
    secret_key: str = 'test'
    algorithm: str = 'test'
    access_token_expire_minutes: int = 30

    class Config:
        env_file = "../.env"
        # env_file = "./.env"


settings = Settings()