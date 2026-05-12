def test_user_login():
    print("Hello, this is a test function for user login.")


class TestUserLogin:
    def test_user_login(self):
        print("Hello, this is a test method for user login.")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "Expected 2 + 2 to equal 5, but it does not."