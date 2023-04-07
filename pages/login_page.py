from pages.base_page import BasePage


class LoginPage(BasePage):
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    login_field_xpath ="//*[@id='login']"
    password_field_xpath = "//*[contains(@name,'password')]"
    scouts_panel_text_xpath = "//*[text()='Scouts Panel']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    english_language_xpath = "//*[text()='English']"
    email_field_xpath = "//*[text()='E-mail']"
    back_to_sign_in_hyperlink_xpath = "//*[text()='Back to sign in']"
    send_button_xpath ="//*[text()='Send']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
