from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Non-secret config
    app_name: str = "lists"
    server_port: int = 9000
    debug: bool = False

    # Database config (secrets from .env or environment)
    postgres_host: str = Field(..., env="POSTGRES_HOST")
    PGPORT: int = Field(..., env="PGPORT")
    postgres_db: str = Field(..., env="POSTGRES_DB")
    postgres_user: str = Field(..., env="POSTGRES_USER")

    # JWT config (secrets from .env or environment)
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = "HS256"

    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://{self.postgres_user}"
            f"@{self.postgres_host}:{self.PGPORT}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra config values not explicitly defined


settings = Settings()
