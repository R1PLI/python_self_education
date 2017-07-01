import pytest

from selene.browser import driver, set_driver
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    set_driver(webdriver.Chrome)

    def teardown():
        driver().quit()

    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass