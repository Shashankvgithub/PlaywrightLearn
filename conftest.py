import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    ),
    parser.addoption(
        "--url", action="store", default="https://rahulshettyacademy.com/client", help="URL Selection"
    )

@pytest.fixture(scope="function")
def browserInstance(playwright,page,request):
    browser_name=request.config.getoption("browser_name")
    url=request.config.getoption("url")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True,args=['--start-maximized']) #args=['--start-maximized']
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True,args=['--start-maximized']) #args=['--start-maximized']

    context = browser.new_context(no_viewport=True)
    # page = context.new_page()
    page.goto(url)
    yield page
    context.close()
    browser.close()

# Sample

