import os

import dotenv
from pydantic import BaseModel


class Settings(BaseModel):
    dotenv.load_dotenv()
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('KEYSPACE')
    remote_url: str = os.getenv('REMOTE_URL')
    deviceName: str = os.getenv('DEVICE_NAME', 'Google Pixel 7')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    app: str = os.getenv('APP')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    timeout: float = os.getenv('TIMEOUT')
