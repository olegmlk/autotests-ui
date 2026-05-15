import pytest

SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="System version is too old for this test."
)
def test_system_version_valid():
    ... # code to check if the system version is valid

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="System version is too old for this test."
)
def test_system_version_invalid():
    ... # code to check if the system version is invalid