import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser, support

import config
import utils
from utils.file import abs_path_from_project


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        required=False,
        default="local_emulator",
        choices=['local_emulator', 'bs', 'local_real'],
    )

def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(dotenv_path=f'/Users/rollnick/Desktop/QAGuruProjects/QAGuru9_21/.env.{context}')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")

@pytest.fixture(scope='function', autouse=True)
def new_management(context):
    from config import config

    options = config.to_driver_options(context=context)

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            options.get_capability('remote_url'),
            options=options
        )

    browser.config.timeout = 10.0

    yield

    utils.allure.attach_screenshot()
    utils.allure.attach_logs()
    with allure.step('tear down app session'):
        browser.quit()


@pytest.fixture()
def real_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': config.config.platformName,
        'udid': config.config.udid,
        'appWaitActivity': config.config.appWaitActivity,
        'app': abs_path_from_project(config.config.app)
    })

    browser.config.driver = webdriver.Remote(
        'http://127.0.0.1:4723/wd/hub',
        options=options
    )

    yield

    utils.allure.attach_screenshot()
    utils.allure.attach_logs()
    with allure.step('tear down app session'):
        browser.quit()


@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': config.config.platformVersion,
        'deviceName': config.config.deviceName,
        'app': config.config.app,
        'appWaitActivity': config.config.appWaitActivity,
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': config.config.USER_NAME,
            'accessKey': config.config.ACCESS_KEY,
        }
    })
    browser.config.timeout = config.config.timeout

    browser.config.driver = webdriver.Remote(
        config.config.remote_url,
        options=options
    )

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    session_id = browser.driver.session_id
    utils.allure.attach_screenshot()
    utils.allure.attach_logs()
    with allure.step('tear down app session'):
        browser.quit()
    utils.allure.attach_bstack_video(session_id)
