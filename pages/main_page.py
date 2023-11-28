from time import sleep

from selenium.webdriver.common.by import By

from pages.base import Base


class MainPage(Base):

    def __init__(self, driver_inst):
        super().__init__(driver_inst)

    locaters = {
        "search_input_box": "//input[@placeholder='Search']",
        "search_button": "//button[@aria-label='search']",
        "row": "//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']",
        "column": "//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td",
        "rows_per_page": "//p[@id='mui-3']",
        "rows_per_page_value": "#mui-2",
        "displayed_rows_icon": "//p[@class='MuiTablePagination-displayedRows css-11ceysh-MuiTablePagination-displayedRows']",
        "next_page_button": "//button[@title='Go to next page']//*[name()='svg']",
        "back_page_button": "//button[@title='Go to previous page']//*[name()='svg']",
        "no_data_found_msg": "//h6[@class='MuiTypography-root MuiTypography-subtitle1 MuiTypography-alignCenter css-w0mrp1-MuiTypography-root']",
        "rate_limit_error": "//h2[@id='swal2-title']",
        "loading_icon": "//div[@data-testid='bars-loading']//*[name()='svg']"
    }

    def input_search_box(self, text):
        self.presence_element(strategy=By.XPATH, selector=self.locaters['search_input_box']).clear()
        self.presence_element(strategy=By.XPATH, selector=self.locaters['search_input_box']).send_keys(text)

    def click_search_button(self):
        self.presence_element(strategy=By.XPATH, selector=self.locaters['search_button']).click()

    def get_rows(self):
        elements = self.presence_elements(strategy=By.XPATH, selector=self.locaters['row'], stop=False)
        return elements

    def get_name_column_values(self):
        names = self.presence_elements(strategy=By.XPATH,
                                       selector="//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td[1]")
        return names

    def get_owner_column_values(self):
        owners = self.presence_elements(strategy=By.XPATH,
                                        selector="//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td[2]")
        return owners

    def get_stars_column_values(self):
        stars = self.presence_elements(strategy=By.XPATH,
                                       selector="//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td[3]")
        return stars

    def get_link_column_values(self):
        links = self.presence_elements(strategy=By.XPATH,
                                       selector="//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td[4]")
        return links

    def get_details_column_values(self):
        details = self.presence_elements(strategy=By.XPATH,
                                         selector="//tr[@class='MuiTableRow-root css-k6k3l1-MuiTableRow-root']/td[5]")
        return details

    def get_rows_per_page_icon(self):
        return self.presence_element(strategy=By.XPATH, selector=self.locaters["rows_per_page"]).text

    def get_rows_per_page_value(self):
        return self.presence_element(strategy=By.CSS_SELECTOR, selector=self.locaters["rows_per_page_value"]).text

    def click_rows_per_page_select(self):
        self.clickable_element(strategy=By.CSS_SELECTOR, selector=self.locaters["rows_per_page_value"]).click()

    def click_rows_option(self, rows):
        self.presence_element(strategy=By.XPATH, selector="//li[normalize-space()='" + rows + "']").click()

    def get_displayed_rows_value(self):
        return self.presence_element(strategy=By.XPATH, selector=self.locaters["displayed_rows_icon"]).text

    def click_next_page_button(self):
        self.clickable_element(strategy=By.XPATH, selector=self.locaters["next_page_button"]).click()

    def get_next_page_button(self):
        return self.presence_element(strategy=By.XPATH, selector=self.locaters["next_page_button"])

    def click_back_page_button(self):
        self.clickable_element(strategy=By.XPATH, selector=self.locaters["back_page_button"]).click()

    def get_back_page_button(self):
        return self.presence_element(strategy=By.XPATH, selector=self.locaters["back_page_button"])

    def get_no_data_found_msg(self):
        return self.presence_element(strategy=By.XPATH, selector=self.locaters["no_data_found_msg"]).text

    def get_rate_limit_error(self):
        return self.displayed_element(strategy=By.XPATH, selector=self.locaters["rate_limit_error"], stop=False)

    def wait_for_loading(self):
        sleep(5)
        self.invisible_element(strategy=By.XPATH, selector=self.locaters["loading_icon"])
        return
