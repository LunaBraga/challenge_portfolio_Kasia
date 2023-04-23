import time

from pages.base_page import BasePage

class Report(BasePage):
    reports_url = 'https://scouts-test.futbolkolektyw.pl/en/players/62f02fa32d2b7461da157b0f/reports/63c283dd1cabf1171d40c177/edit'
    expected_title = "Scouts Panel"
    reports_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]/div[2]/span"

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_reports_button(self):
        self.click_on_the_element(self.reports_button_xpath)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title
