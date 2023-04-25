import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = '//*[@title="Logo Scouts Panel"]'
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    wait = WebDriverWait(driver, 10)
    main_page_hyperlink_xpath = "//*[contains(@class, 'MuiTypography-root')]"
    players_text_xpath = "//*[text()='Players']"
    english_language_xpath = "//*[text()='English']"
    language_field_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_text_xpath = "//*[text()='Players count']"
    count_text_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    event_count_text_xpath = "//*[text()='Events count']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    super_man_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"
    added_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    expected_text = "Anna Stone"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title() == self.expected_title

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_super_man_button(self):
        self.click_on_the_element(self.super_man_button_xpath)

    def click_on_the_polski_button(self):
        self.click_on_the_element(self.language_field_xpath)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def comparing_text(self):
        time.sleep(5)
        self.assert_element_text(self.driver, self.added_player_xpath, self.expected_text)
