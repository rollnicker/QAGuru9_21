import os
from typing import Literal

import dotenv
from pydantic import BaseModel
from appium.options.android import UiAutomator2Options


context_type = Literal["bs", "local_emulator", "local_real"]
class Config(BaseModel):
    dotenv.load_dotenv('/Users/rollnick/Desktop/QAGuruProjects/QAGuru9_21/.env.local_real')
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('KEYSPACE')
    remote_url: str = os.getenv('REMOTE_URL')
    deviceName: str = os.getenv('DEVICE_NAME', 'Google Pixel 7')
    udid: str = os.getenv('UDID')
    platformVersion: str = os.getenv('PLATFORM_VERSION', '13.0')
    app: str = os.getenv('APP', 'bs://sample.app')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    platformName: str = os.getenv('PLATFORM_NAME')
    # timeout: float = 5.0

    def to_driver_options(self, context):

        options = UiAutomator2Options()

        if context == 'local_real':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app)
            options.set_capability('platformName', self.platformName)

        return options


config = Config(context="local_emulator")
