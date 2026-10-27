from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    database_url: str = 'sqlite:///./dev.db'
    log_level: str = 'INFO'
    app_version: str = '1.0.0'


settings = Settings()
