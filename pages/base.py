from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utility.logger import logger


class Base:
    def __init__(self, driver_inst):
        self.driver = driver_inst

    def presence_elements(self, strategy, selector, wait_time=6, poll_frequency=0.5, stop=True):
        try:
            return WebDriverWait(self.driver, wait_time, poll_frequency).until(
                expected_conditions.presence_of_all_elements_located((strategy, selector)))
        except TimeoutException as e:
            if stop:
                raise e
            else:
                logger.debug('No elements found')
                return None

    def clickable_element(self, strategy, selector, wait_time=6, poll_frequency=0.5, stop=True):
        return WebDriverWait(self.driver, wait_time, poll_frequency, stop).until(
            expected_conditions.element_to_be_clickable((strategy, selector)))

    def __presence_element(self, elements, selector, stop):
        try:
            return elements[0]
        except IndexError:
            if stop:
                raise Exception('no presence element matched the selector: {}'.format(selector))

    def presence_element(self, strategy, selector, wait_time=6, poll_frequency=0.5, stop=True):
        elements = self.presence_elements(strategy, selector, wait_time, poll_frequency, stop)
        return self.__presence_element(elements, selector, stop)

    def refresh(self):
        self.driver.refresh()

    def displayed_element(self, strategy, selector, wait_time=6, poll_frequency=0.5, stop=True):
        elements = self.presence_elements(strategy, selector, wait_time, poll_frequency, stop)
        if not elements:
            return None
        if elements[0].is_displayed():
            return True
        else:
            logger.debug('Element not visible')
            return False

    def invisible_element(self, strategy, selector, wait_time=6, poll_frequency=0.5, stop=True):
        return WebDriverWait(self.driver, wait_time, poll_frequency).until(
            expected_conditions.invisibility_of_element_located((strategy, selector)))
