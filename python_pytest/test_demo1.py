# pytest example
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello, World!")

@pytest.mark.skip
def test_secondProgram():
    print("Hello, again!")
    assert 1 == 2, "This assertion will fail"


    
 