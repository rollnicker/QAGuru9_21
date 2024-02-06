import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    bstack_userName: str = os.getenv('bstack_userName')
    bstack_accessKey: str = os.getenv('bstack_accessKey')
    remote_url: str = os.getenv('remote_url')
    deviceName: str = 'Google Pixel 7'
    platformVersion: str = "13.0"
    app: str = 'bs://sample.app'
    timeout: float = 10.0


settings = Settings()
