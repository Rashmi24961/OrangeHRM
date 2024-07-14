import pytest
from selenium import webdriver
from utilities import readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser=readconfigurations.read_configurations("Basic Info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url=readconfigurations.read_configurations("Basic Info","url")
    driver.get(app_url)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver=driver
    yield
    driver.quit()