import time

from pages.base_page import BasePage

class AddaPlayer(BasePage):
    add_player_text_xpath = "//*[text()='Add player']"
    email_field_xpath = "//*[contains(@class, 'MuiInputBase')]"
    email_text_xpath = "//*[text()='E-mail']"
    phone_text_xpath = "//*[text()='Phone']"
    level_text_xpath = "//*[text()='Level']"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    district_field_xpath = "//*[@id='mui-component-select-district']"
    clear_button_xpath = "//*[text()='Clear']"
    required_text_xpath = "//*[text()='Required']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    expected_title = "Add player"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_button_title(self):
        time.sleep(5)
        assert self.get_button_title() == self.expected_title


