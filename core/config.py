from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Non-secret config
    app_name: str = "lists"
    server_port: int = 9069
    debug: bool = False

    # Database config: pulls from .env or environment
    database_url: str = "sqlite:///./lists.db"

    # JWT config
    secret_key: str
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
