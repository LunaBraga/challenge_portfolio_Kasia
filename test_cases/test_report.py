import os
import unittest
import time

from selenium import webdriver

from pages.Add_a_Player import AddaPlayer
from pages.Dashboard import Dashboard
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.report import Report
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestReport(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_report(self):
        user_login = LoginPage(self.driver)
        user_login.check_login_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_super_man_button()
        players = Report(self.driver)
        players.click_on_the_reports_button()
        players.click_on_the_add_report_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()