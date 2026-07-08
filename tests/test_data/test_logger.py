import sys

sys.path.append("src")

from placementiq.common.logger import logger


def test_logger():
    logger.info("Logger initialized successfully.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")


if __name__ == "__main__":
    test_logger()
