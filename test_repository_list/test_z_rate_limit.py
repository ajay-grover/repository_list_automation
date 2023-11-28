from time import sleep

from utility.logger import logger


class TestZRateLimit:
    def test_rate_limit_error(self, setup):
        logger.info(f"Executing test_rate_limit_error")
        setup.input_search_box('ajay')
        setup.click_search_button()
        setup.wait_for_loading()
        count = 1
        f = 0
        while True and count <= 20:
            setup.click_next_page_button()
            count = count + 1
            if setup.get_rate_limit_error():
                f = 1
                break

        if f == 0:
            raise AssertionError('Failed to see rate_limit_error')
