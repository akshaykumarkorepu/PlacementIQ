import sys

sys.path.append("src")

from placementiq.settings.settings import settings


def test_settings():
    print("Project Name :", settings.project_name)
    print("Debug Mode   :", settings.debug)
    print("Database Path:", settings.database_path)
    print("Log Level    :", settings.log_level)
    print("Data Folder  :", settings.data_directory)


if __name__ == "__main__":
    test_settings()
