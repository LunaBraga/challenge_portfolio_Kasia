import time

from pages.base_page import BasePage


class Report(BasePage):
    reports_url = "https://scouts-test.futbolkolektyw.pl/en/players/62f02fa32d2b7461da157b0f/reports/63c283dd1cabf1171d40c177/edit"
    futbol_kolektyw_button_xpath = '//*[@title="Logo Scouts Panel"]'
    reports_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]/div[2]/span"
    add_report_button_xpath = "//*[@id='__next']/div[1]/main/a/button/span[1]"
    expected_title = "Scouts panel"

    def title_of_page(self):
        self.wait_for_visibility_of_element_located(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title() == self.expected_title

    def click_on_the_reports_button(self):
        self.click_on_the_element(self.reports_button_xpath)

    def click_on_the_add_report_button(self):
        self.click_on_the_element(self.add_report_button_xpath)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title
