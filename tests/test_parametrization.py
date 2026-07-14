import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0, f"Number {number} is not greater than zero."

@pytest.mark.parametrize('number, expected', [(1,1), (2, 4), (3, 9), (-1, 1)])
def test_several_numbers(number, expected):
    assert number**2 == expected, f"Square of {number} is not equal to {expected}."


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multibrowsers(os, browser):
    print(f"Running test on {os} with {browser} browser.")
    assert os in ['macos', 'windows', 'linux'], f"OS {os} is not supported."
    assert browser in ['chromium', 'webkit', 'firefox'], f"Browser {browser} is not supported."


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")

@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit Card', 'Debit Card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f"Testing operations for user: {user} with account: {account}")

    def test_user_without_operations(self, user: str):
        print(f"Testing user without operations: {user}")


users = {'+1234567890': 'user with money',
        '+0087654321': 'user without money',
        '+1122334455': 'user with pending transactions'}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)

def test_identifiers(phone_number: str):
    print(f"Testing with phone number: {phone_number}")
    ...