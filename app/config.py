from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # app
    app_name: str = "AI Lead Intelligence Agent"
    app_env: str = "development"
    debug: bool = False
    api_version: str = "v1"

    # security
    secret_key: str = "change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 24hrs
    refresh_token_expire_days: int = 7

    # supabase / postgres — needs asyncpg driver
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/ai_lead_gen"

    # ai
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    # data sources
    serp_api_key: str = ""
    news_api_key: str = ""
    hunter_api_key: str = ""
    apollo_api_key: str = ""

    # email
    sendgrid_api_key: str = ""
    sendgrid_from_email: str = ""
    sendgrid_from_name: str = "AI Lead Agent"
    sendgrid_webhook_secret: str = ""

    # pipeline
    auto_approve_emails: bool = False  # set True to skip manual approval
    max_emails_per_day: int = 100
    max_emails_per_hour: int = 20
    pipeline_schedule_hour: int = 6  # runs daily at 6am

    # redis
    redis_url: str = "redis://localhost:6379"

    # monitoring
    sentry_dsn: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
