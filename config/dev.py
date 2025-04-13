import os
from base import BaseConfig

class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 123
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5001

    DETECTION_MODEL = "openai/clip-vit-base-patch32"
    NSFW_MODEL = "Falconsai/nsfw_image_detection"

    UPLOAD_FOLDER = os.path.join('static', 'temp')
    FILE_NAME = ''

    MINIO_URL = 'http://localhost:9000'
    MINIO_ACCESS_KEY = 'your-access-key'
    MINIO_SECRET_KEY = 'your-secret-key'
    MINIO_BUCKET = 'images'