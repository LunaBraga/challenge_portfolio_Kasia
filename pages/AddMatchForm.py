from pages.base_page import BasePage


class AddMatchForm(BasePage):
       add_player_text_xpath = "//*[text()='Add player']"
       email_field_xpath = "//*[contains(@class, 'MuiInputBase')]"
       email_text_xpath = "//*[text()='E-mail']"
       phone_text_xpath = "//*[text()='Phone']"
       level_text_xpath = "//*[text()='Level']"
       leg_field_xpath = "//*[@id='mui-component-select-leg']"
       district_field_xpath = "//*[@id='mui-component-select-district']"
       clear_button_xpath = "//*[text()='Clear']"
       required_text_xpath = "//*[text()='Required']"
       add_link_to_you_tube_button_text_xpath = "//*[text()='Add link to Youtube']"
pass