from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Policy RAG App"

    DATA_DIR: Path = Path("data")
    RAW_DIR: Path = DATA_DIR / "raw"
    VECTORSTORE_DIR: Path = DATA_DIR / "vectorstore"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_PROVIDER: str = "dummy"

    class Config:
        env_file = ".env"


settings = Settings()
