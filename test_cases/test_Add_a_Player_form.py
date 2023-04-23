import os
import unittest
import time

from selenium import webdriver

from pages.Add_a_Player import AddaPlayer
from pages.Dashboard import Dashboard
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddaPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_Add_a_Player_form(self):
        user_login = LoginPage(self.driver)
        user_login.check_login_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player_button()
        player = AddaPlayer(self.driver)
        player.check_page_title()
        player.type_in_email('house')
        player.type_in_name('Anna')
        player.type_in_surname('Stone')
        player.type_in_phone('+48678903234')
        player.type_in_weight('58kg')
        player.type_in_height('170')
        player.type_in_age('23.12.2000')
        player.click_on_the_right_leg()
        player.type_in_club('Eagles')
        player.type_in_level('5')
        player.type_in_main_position('3')
        player.type_in_second_position('2')
        player.click_on_the_lower_silesia()
        player.type_in_achievements('34')
        player.type_in_laczy_nas_pilka('2344')
        player.type_in_minut('34')
        player.type_in_facebook('234567')
        player.click_on_the_submit_button()
        time.sleep(5)