import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture(params=['chrome', 'firefox', 'edge', 'safari'])
# @pytest.fixture()
def driver(request):
    # browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating {browser} webdriver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(options=options)
    elif browser == "safari":
        my_driver = webdriver.Safari()
    elif browser == "edge":
        my_driver = webdriver.Edge()
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected browsers: 'chrome' or 'safari' or 'edge' or 'firefox' but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} webdriver")
    my_driver.quit()
