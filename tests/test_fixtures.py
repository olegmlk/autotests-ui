from symtable import Class

import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE], sending analytics data:")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION], loading settings...")


@pytest.fixture(scope="class")
def user():
    print("[CLASS], creating a user instance...")


@pytest.fixture(scope="function")
def browser(user):
    print("[FUNCTION], launching a browser instance for the user...")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        print("Testing user login...")

    def test_user_can_create_course(self, user, browser):
        print("Testing course creation...")


class TestAccountFlow:
    def test_user_account(self, user, browser):
        print("Testing user account...")
