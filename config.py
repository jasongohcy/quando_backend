import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or os.urandom(32)


class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False
    # GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    # GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True

