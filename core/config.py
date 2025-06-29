from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Non-secret config
    app_name: str = "lists"
    server_port: int = 9000
    debug: bool = False

    # Database config (secrets from .env or environment)
    postgres_host: str = Field("localhost", env="POSTGRES_HOST")
    postgres_port: int = Field(5432, env="POSTGRES_PORT")
    postgres_db: str = Field("lists", env="POSTGRES_DB")
    postgres_user: str = Field("postgres", env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")


    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"

settings = Settings()
