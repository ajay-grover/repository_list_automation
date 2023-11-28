import pytest
import os
from selenium import webdriver
from seleniumrequests import Remote, Chrome, Safari
from pages.main_page import MainPage
from utility.logger import logger


@pytest.fixture(scope='session', autouse=True)
def initiate_driver():
    logger.info('initiate driver')
    cops = webdriver.ChromeOptions()
    cops.add_argument('ignore-certificate-errors')
    cops.add_argument('--allow-insecure-localhost')
    cops.add_argument("start-maximized")
    caps = cops.to_capabilities()
    caps['acceptInsecureCerts'] = True
    selenium_url = os.getenv('SELENIUM_URL')
    driver = Chrome(selenium_url, chrome_options=cops, desired_capabilities=caps)
    # return driver
    yield driver
    driver.quit()


# def open_page(driver,base_url):
#     if self.url is None:
#         raise RuntimeError('url must be specified')
#     self.driver.get(self.url)
#     return self

@pytest.fixture(scope='class', autouse=True)
def setup(initiate_driver):
    logger.info('running setup')
    initiate_driver.get('http://localhost:3000/')
    main_page = MainPage(initiate_driver)
    return main_page
