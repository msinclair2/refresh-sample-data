from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env')

    token: str = Field(alias="TOKEN")
    base_url: str = Field(alias="BASE_URL")
    dataset_id: str = Field(alias="DATASET_ID")
    raw_pipeline_id: str = Field(alias="RAW_PIPELINE_ID")
    processed_pipeline_id: str = Field(alias="PROCESSED_PIPELINE_ID")