import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.login_page import LoginPage

@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "Password")
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    print(
        "This test simulates an unsuccessful user authorization process with wrong email or password."
    )
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email, password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

    # chromium_page.goto(
    #     "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    # )
    #
    # email_input = chromium_page.get_by_test_id("login-form-email-input").locator(
    #     "input"
    # )
    # email_input.fill(email)
    #
    # password_input = chromium_page.get_by_test_id("login-form-password-input").locator(
    #     "input"
    # )
    # password_input.fill(password)
    #
    # login_button = chromium_page.get_by_test_id("login-page-login-button")
    # login_button.click()
    #
    # wrong_email_or_password_alert = chromium_page.get_by_test_id(
    #     "login-page-wrong-email-or-password-alert"
    # )
    # expect(wrong_email_or_password_alert).to_be_visible()
    # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
    chromium_page.wait_for_timeout(2000)
