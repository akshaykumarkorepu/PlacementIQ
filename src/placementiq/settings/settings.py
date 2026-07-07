import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.project_name = os.getenv("PROJECT_NAME", "PlacementIQ")
        self.debug = os.getenv("DEBUG", "false").lower() == "true"

        self.database_path = os.getenv("DATABASE_PATH", "data/placementiq.sqlite")

        self.log_level = os.getenv("LOG_LEVEL", "INFO")

        self.data_directory = os.getenv("DATA_DIRECTORY", "data")


settings = Settings()
