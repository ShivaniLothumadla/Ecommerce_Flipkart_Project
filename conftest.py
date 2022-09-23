import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True, scope='class')
def setup(request, browser, url='https://www.flipkart.com/'):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'ff':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--url')


@pytest.fixture(autouse=True, scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(autouse=True, scope='session')
def url(request):
    return request.config.getoption('--url')
