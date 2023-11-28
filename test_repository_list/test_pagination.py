import pytest
from utility.logger import logger


class TestPagination:
    def test_rows_per_page(self, setup):
        logger.info(f"Executing test_rows_per_page")
        setup.input_search_box('ajay')
        setup.click_search_button()
        setup.wait_for_loading()
        assert setup.get_rows_per_page_icon() == "Rows per page:", "Failed to assert rows per page icon"
        assert setup.get_rows_per_page_value() == "10", "Failed to assert rows per page value"
        displayed_pages_value = setup.get_displayed_rows_value()
        assert displayed_pages_value.split(' ')[0] == "1–10"

    @pytest.mark.parametrize("input_count", [10, 25, 50])
    def test_rows_per_page_options(self, setup, input_count):
        logger.info(f"Executing test_rows_per_page_options for input {input_count}")
        start = 1
        end = input_count
        setup.click_rows_per_page_select()
        setup.click_rows_option(str(input_count))
        setup.wait_for_loading()
        assert setup.get_rows_per_page_icon() == "Rows per page:", "Failed to assert rows per page icon"
        assert setup.get_rows_per_page_value() == str(input_count), "Failed to assert rows per page value"
        rows = setup.get_rows()
        assert len(rows) == input_count, 'Failed to assert count of rows'
        displayed_pages_value = setup.get_displayed_rows_value()
        assert displayed_pages_value.split(' ')[0] == str(start)+"–" + str(end)
        logger.info(f"testing next button")
        setup.click_next_page_button()
        start = start + input_count
        end = end + input_count
        setup.wait_for_loading()
        rows = setup.get_rows()
        assert len(rows) == input_count, 'Failed to assert count of rows'
        assert setup.get_rows_per_page_icon() == "Rows per page:", "Failed to assert rows per page icon"
        assert setup.get_rows_per_page_value() == str(input_count), "Failed to assert rows per page value"
        displayed_pages_value = setup.get_displayed_rows_value()
        assert displayed_pages_value.split(' ')[0] == str(start)+"–" + str(end)
        logger.info(f"testing back button")
        setup.click_back_page_button()
        start = start - input_count
        end = end - input_count
        setup.wait_for_loading()
        rows = setup.get_rows()
        assert len(rows) == input_count, 'Failed to assert count of rows'
        assert setup.get_rows_per_page_icon() == "Rows per page:", "Failed to assert rows per page icon"
        assert setup.get_rows_per_page_value() == str(input_count), "Failed to assert rows per page value"
        displayed_pages_value = setup.get_displayed_rows_value()
        assert displayed_pages_value.split(' ')[0] == str(start) + "–" + str(end)

