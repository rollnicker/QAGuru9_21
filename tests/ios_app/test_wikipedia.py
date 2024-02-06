from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_sample_app(ios_management):
    with step('Type something'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys("hello@browserstack.com" + "\n")
    with step('Check results'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("hello@browserstack.com"))
