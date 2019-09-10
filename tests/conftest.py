import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ALLOWED_LANGUAGES = ('es', 'fr', 'ru', 'en', )


def pytest_addoption(parser):
    """add support for new command line arguments"""
    parser.addoption(
        '--language', action='store',
        choices=ALLOWED_LANGUAGES, default='en', help="Choose the language",
    )
    parser.addoption(
        '--headless', action='store_true', help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def user_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("headless")


@pytest.fixture(scope="session")
def options(request, headless, user_language):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument(f"--lang={user_language}")
    else:
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options


@pytest.fixture(scope="function")
def browser(options):
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
