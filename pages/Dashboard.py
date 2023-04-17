import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    main_page_hyperlink_xpath = "//*[contains(@class, 'MuiTypography-root')]"
    players_text_xpath = "//*[text()='Players']"
    english_language_xpath = "//*[text()='English']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_text_xpath = "//*[text()='Players count']"
    count_text_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    event_count_text_xpath = "//*[text()='Events count']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title
    def click_on_the_add_player_button(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_button_xpath)



