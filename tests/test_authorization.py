import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.authorization
@pytest.mark.regression
def test_wrong_email_or_password_authorization(chromium_page: Page):
    print("This test simulates an unsuccessful user authorization process with wrong email or password.")
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('Password')

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
    chromium_page.wait_for_timeout(2000)