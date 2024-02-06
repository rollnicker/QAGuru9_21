import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    bstack_userName: str = os.getenv('USERNAME')
    bstack_accessKey: str = os.getenv('ACCESKEY')
    remote_url: str = os.getenv('REMOTE_URL')
    deviceName: str = 'Google Pixel 7'
    platformVersion: str = "13.0"
    app: str = 'bs://sample.app'
    timeout: float = 5.0


settings = Settings()
