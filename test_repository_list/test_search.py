
import pytest

from assertpy import assert_that

from utility.api_util import ApiUtility
from utility.logger import logger


class TestSearch:

    @pytest.mark.parametrize("input_text", ["ajayyy", "docker11", "ajayyyy", "@@"])
    def test_search(self, setup, input_text):
        logger.info(f'test_search for {input_text}')
        setup.input_search_box(input_text)
        setup.click_search_button()
        setup.wait_for_loading()
        assert setup.get_rows_per_page_icon() == "Rows per page:", "Failed to assert rows per page icon"
        assert setup.get_rows_per_page_value() == "10", "Failed to assert rows per page value"

        rows = setup.get_rows()
        if rows is None:
            assert setup.get_no_data_found_msg() == "No Data Found", "Failed to assert  no data found msg"
            assert setup.get_displayed_rows_value() == "0–0 of 0", "Failed to assert displayed rows value"
        else:
            res = ApiUtility().search_repositories(input_text)
            logger.debug(f'response :{res}')
            total_count = res.get('total_count')
            count = total_count

            start = 1
            end = 10
            while count > 10:
                rows = setup.get_rows()
                assert len(rows) == 10, 'Failed to assert count of rows'
                names = setup.get_name_column_values()
                assert_that(names, 'Failed to assert names').does_not_contain(None)
                owners = setup.get_owner_column_values()
                assert_that(owners, 'Failed to assert owners').does_not_contain(None)
                stars = setup.get_owner_column_values()
                assert_that(stars, 'Failed to assert stars').does_not_contain(None)
                links = setup.get_link_column_values()
                assert_that(links, 'Failed to assert links').does_not_contain(None)
                details = setup.get_details_column_values()
                assert_that(details, 'Failed to assert details').does_not_contain(None)

                expected_pages = f'{start}–{end} of {total_count}'
                assert setup.get_displayed_rows_value() == expected_pages, 'Failed to assert displayed_pages_value'

                setup.click_next_page_button()
                start = start + 10
                end = end + 10
                setup.wait_for_loading()
                if end > total_count:
                    end = total_count
                count = count - 10
            expected_pages = f'{start}–{total_count} of {total_count}'
            rows = setup.get_rows()
            assert len(rows) == count, 'Failed to assert count of rows'
            assert setup.get_displayed_rows_value() == expected_pages, "Failed to assert displayed rows value"
            names = setup.get_name_column_values()
            assert_that(names, 'Failed to assert names').does_not_contain(None)
            owners = setup.get_owner_column_values()
            assert_that(owners, 'Failed to assert owners').does_not_contain(None)
            stars = setup.get_owner_column_values()
            assert_that(stars, 'Failed to assert stars').does_not_contain(None)
            links = setup.get_link_column_values()
            assert_that(links, 'Failed to assert links').does_not_contain(None)
            details = setup.get_details_column_values()
            assert_that(details, 'Failed to assert details').does_not_contain(None)
