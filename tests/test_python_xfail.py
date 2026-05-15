import pytest


@pytest.mark.xfail(reason="This test is expected to fail due to a known bug.")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="This test is expected to fail due to a known issue.")
def test_with_known_issue():
    ...

