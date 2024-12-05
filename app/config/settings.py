from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    forecaster_path: str = "app/data/forecaster.pkl"
    target_path: str = "app/data/target.pkl"

    training_data_path: str = "app/data/training_data.csv"

    app_name: str = "Open Heart API"
    version: str = "1.0.0"

    class Config:
        env_file = ".env" 


settings = Settings()
