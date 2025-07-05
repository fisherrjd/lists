from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Non-secret config
    app_name: str = "lists"
    server_port: int = 9000
    debug: bool = False

    # Database config (secrets from .env or environment)
    postgres_host: str
    PGPORT: int
    postgres_db: str
    postgres_user: str

    # JWT config (secrets from .env or environment)
    secret_key: str
    algorithm: str = "HS256"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}"
            f"@{self.postgres_host}:{self.PGPORT}/{self.postgres_db}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
