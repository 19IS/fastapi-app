import os
from pathlib import Path

from dotenv import load_dotenv

APP_ROOT = Path(__file__).resolve().parent.parent
ENVIRONMENT = 'docker-compose.env'

load_dotenv(
    dotenv_path=Path.joinpath(APP_ROOT, ENVIRONMENT)
)

FASTAPI_HOST = str(os.getenv('FASTAPI_HOST'))
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT'))

STATIC_FILES_DIR = 'src/static/'
TEMPLATES_DIR = 'src/templates/'

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_INITDB_DATABASE = os.getenv('MONGO_INITDB_DATABASE')
MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME')
MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
