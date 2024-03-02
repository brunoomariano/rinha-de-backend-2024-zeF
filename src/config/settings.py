from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  DB_NAME: str = Field(alias="POSTGRES_DB", default="postgres")
  DB_USER: str = Field(alias="POSTGRES_USER", default="postgres")
  DB_PASSWORD: str = Field(alias="POSTGRES_PASSWORD", default="postgres")
  DB_HOST: str = Field(alias="POSTGRES_HOST", default="localhost")
  DB_PORT: int = Field(alias="POSTGRES_PORT", default=5432)