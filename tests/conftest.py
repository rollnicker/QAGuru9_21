import allure
import allure_commons
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver import webdriver
from selene import browser, support

import config
import utils


@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': config.settings.platformVersion,
        'deviceName': config.settings.deviceName,
        'app': config.settings.app,
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': config.settings.USERNAME,
            'accessKey': config.settings.ACCESKEY,
        }
    })
    browser.config.timeout = config.settings.timeout

    browser.config.driver_remote_url = config.settings.remote_url
    browser.config.driver_options = options

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


@pytest.fixture(scope='function')
def ios_management():
    options = XCUITestOptions().load_capabilities({
        "deviceName": "iPhone 11 Pro",
        "platformName": "ios",
        "platformVersion": "13",
        'app': config.settings.app,

        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': config.settings.USERNAME,
            'accessKey': config.settings.ACCESKEY,
        }
    })
    browser.config.timeout = config.settings.timeout

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url,
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
