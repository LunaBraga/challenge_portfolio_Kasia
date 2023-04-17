from pages.base_page import BasePage


class LoginPage(BasePage):
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@class,'MuiButton-label')]"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    english_language_xpath = "//*[text()='English']"
    login_field_xpath = "//*[@id='login']"
    back_to_sign_in_hyperlink_xpath = "//*[text()='Back to sign in']"
    send_button_xpath = "//*[text()='Send']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_login_title(self):
        assert self.get_page_title() == self.expected_title
