from pydantic import BaseSettings


# Add all of the secrets and configurable variables here, you can also set a default value here.
class Setting(BaseSettings):
    database_type: str
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire: int
    api_key: str

    class Config:
        env_file = ".env"


settings = Setting()
