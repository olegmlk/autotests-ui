import pytest

@pytest.mark.skip(reason="This test is skipped because the feature is still under development.")
def test_feature_in_development():
    print("This test is skipped because the feature is still under development.")

@pytest.mark.skip(reason="This test is skipped because the feature is still under development.")
class TestSuiteSkip:
    def test_feature_in_development1(self):
        print("This test case is skipped because the feature is still under development.")

    def test_feature_in_development2(self):
        print("This test case will be executed.")