import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



@pytest.fixture()
def setup(browser):
    if browser=='chrome':

        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver
    elif browser=="firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver


    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#####################pytest HTML report############################################

"""def pytest_configure(config):
    config._metadata['Project Name']='nopcommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Danish'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)"""
