import pytest

@pytest.fixture()
def setup():
    print("Setting up the test environment")
    yield
    print("Tearing down the test environment")

@pytest.fixture
def dataLoad():
    print("Loading data for the test")
    return ["data1", "data2", "data3"]

@pytest.fixture(params=["chrome", "firefox", "safari"])
def crossBrowser(request):
    return request.param
