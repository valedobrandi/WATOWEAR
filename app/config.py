from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic will automatically look for OPENAI_API_KEY in the environment or .env file
    openai_api_key: str
    model_name: str = "gpt-4o-mini"  # Defaulting to a cost-effective model
    
    # Tells pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()