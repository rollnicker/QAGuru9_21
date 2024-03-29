import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('KEYSPACE')
    remote_url: str = os.getenv('REMOTE_URL')
    deviceName: str = 'Google Pixel 7'
    platformVersion: str = "13.0"
    app: str = 'bs://sample.app'
    timeout: float = 5.0


settings = Settings()
