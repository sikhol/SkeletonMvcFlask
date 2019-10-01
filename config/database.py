import os
import urllib
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DEBUG = True

class DevelopmentConfig(Config):
    ORATOR_DATABASES = {
        'postgres': {
            'driver': os.getenv('DB_DRIVER'),
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_DATABASE'),
            'user': os.getenv('DB_USERNAME'),
            'password': os.getenv('DB_PASSWORD'),
            'prefix': ''
        }
    }
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    test_driver = os.getenv('TEST_DRIVER')
    params = urllib.parse.quote_plus('DRIVER=%s' % test_driver)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    ORATOR_DATABASES = {
        'postgres': {
            'driver': os.getenv('DB_DRIVER'),
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_DATABASE'),
            'user': os.getenv('DB_USERNAME'),
            'password': os.getenv('DB_PASSWORD'),
            'prefix': ''
        }
    }
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
