import os
import logging

logger = logging.getLogger(__name__)

def get_file_path(directory: str, file_name: str) -> str:
    image_path = os.path.join(directory, file_name)
    logger.debug(f"Resolved file path: {image_path}")

    return image_path
