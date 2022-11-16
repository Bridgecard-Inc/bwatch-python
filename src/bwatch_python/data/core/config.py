import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings, AnyHttpUrl
from pydantic.networks import EmailStr

path = Path.cwd()

env_path = path / ".env"

load_dotenv(dotenv_path=env_path)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "DEVELOPMENT")


if ENVIRONMENT == "PRODUCTION":
    """
    set prod environment variables

    """

    pass

elif ENVIRONMENT == "DEVELOPMENT" or ENVIRONMENT == "LOCAL":
    """
    set dev environment variables

    """
    database_url: str = os.environ.get("DATABASE_URL", None)
    bwatch_database_url: str = os.environ.get("BWATCH_DATA_DATABASE_URL", None) 
    google_config_base64 = os.environ.get("GOOGLE_CONFIG_BASE64", None)
    firebase_web_api_key = os.environ.get("FIREBASE_WEB_API_KEY", None)
    sentry_traces_sample_rate = os.environ.get("SENTRY_DEV_TRACES_SAMPLE_RATE", None)
    sentry_dsn = os.environ.get("SENTRY_DSN", None)
    secret_key = os.environ.get("SECRET_KEY", None) 


else:
    pass


class Settings(BaseSettings):
    """
    Set config variables on settins class

    """

    API_TITLE: str = os.environ.get("API_TITLE", "BRIDGECARD ISSUING AUTH SERVICE API")
    API_ROOT_PATH: str = os.environ.get("API_ROOT_PATH", "/api")
    DATABASE_URL: str = database_url
    BWATCH_DATABASE_URL: str =bwatch_database_url
    GOOGLE_CONFIG_BASE64: str = google_config_base64
    FIREBASE_WEB_API_KEY: str = firebase_web_api_key
    API_V1_0STR: str = "/v1"
    SENTRY_TRACES_SAMPLE_RATE: str = sentry_traces_sample_rate
    SENTRY_DSN: str = sentry_dsn
    SECRET_KEY: str = secret_key


settings = Settings()
