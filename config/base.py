import os

class BaseConfig:
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    SECRET_KEY = 'super-secret-key'