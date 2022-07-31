import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help='Choose language')


@pytest.fixture(scope="function")
def browser(request):

    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    options.add_argument("--headless")
    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.close()