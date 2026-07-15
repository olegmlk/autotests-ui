from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator("input")
        self.password_input = page.get_by_test_id("login-form-password-input").locator("input")
        self.registration_button = self.page.get_by_test_id("login-page-registration-button")

        # testing webhook