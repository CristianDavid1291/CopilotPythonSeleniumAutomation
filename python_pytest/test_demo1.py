# pytest example
import pytest

@pytest.mark.smoke
def test_firstProgram(browserInstance):
    driver = browserInstance
    driver.get("https://www.google.com")

@pytest.mark.skip
def test_secondProgram():
    print("Hello, again!")
    assert 1 == 2, "This assertion will fail"
    