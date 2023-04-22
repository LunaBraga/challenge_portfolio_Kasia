import time

from pages.base_page import BasePage

class AddaPlayer(BasePage):
    add_player_text_xpath = "//*[text()='Add player']"
    email_field_xpath = "//*[contains(@class, 'MuiInputBase')]"
    email_text_add_player_xpath = "//*[text()='E-mail']"
    name_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    phone_text_xpath = "//*[text()='Phone']"
    phone_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    weight_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    height_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    age_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    club_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    level_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    main_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    second_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    achievements_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[14]/div/div/input"
    laczy_nas_pilka_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[16]/div/div/input"
    minut_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[17]/div/div/input"
    facebook_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[18]/div/div/input"
    level_text_xpath = "//*[text()='Level']"
    right_leg_dropdown_xpath = "// *[ @ id = 'menu-leg'] / div[3] / ul / li[1]"
    left_leg_dropdown_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    district_dropdown_xpath = "//*[@id='menu-district']/div[3]/ul/li[1]"
    lower_silesia_dropdown_xpath = "//*[@id='menu-district']/div[3]/ul/li[1]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    clear_text_button_xpath = "//*[text()='Clear']"
    required_text_xpath = "//*[text()='Required']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    player_form_xpath = "//*[contains(@class,'MuiGrid-root')]"
    player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self):
        self.field_send_keys(self.name_field_xpath)

    def type_in_surname(self):
        self.field_send_keys(self.surname_field_xpath)

    def type_in_phone(self):
        self.field_send_keys(self.phone_field_xpath)

    def type_in_weight(self):
        self.field_send_keys(self.weight_field_xpath)

    def type_in_height(self):
        self.field_send_keys(self.height_field_xpath)

    def type_in_age(self):
        self.field_send_keys(self.age_field_xpath)

    def type_in_club(self):
        self.field_send_keys(self.club_xpath)

    def click_on_the_right_leg(self):
        self.click_on_the_element(self.right_leg_dropdown_xpath)

    def type_in_level(self):
        self.field_send_keys(self.level_xpath)

    def type_in_main_position(self):
        self.field_send_keys(self.main_position_xpath)

    def type_in_second_position(self):
        self.field_send_keys(self.second_position_xpath)

    def click_on_the_lower_silesia(self):
        self.click_on_the_element(self.lower_silesia_dropdown_xpath)

    def type_in_achievements(self):
        self.field_send_keys(self.achievements_xpath)


    def type_in_laczy_nas_pilka(self):
        self.field_send_keys(self.laczy_nas_pilka_xpath)

    def type_in_minut(self):
        self.field_send_keys(self.minut_xpath)

    def type_in_facebook(self):
        self.field_send_keys(self.facebook_xpath)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title
