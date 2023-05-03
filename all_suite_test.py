import unittest

from unittest.loader import makeSuite

from test_cases.Login_to_the_system import TestLoginPage
from test_cases.framework import Test
from test_cases.test_Add_a_Player import TestAddaPlayer
from test_cases.test_Add_a_Player_form import TestAddaPlayerForm
from test_cases.test_add_player_form_clear import TestAddaPlayerFormClear
from test_cases.test_change_the_language import TestLoginPageLanguage
from test_cases.test_logout import TestLoginPageLogout
from test_cases.test_report import TestReport


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddaPlayer))
   test_suite.addTest(makeSuite(TestAddaPlayerForm))
   test_suite.addTest(makeSuite(TestAddaPlayerFormClear))
   test_suite.addTest(makeSuite(TestLoginPageLanguage))
   test_suite.addTest(makeSuite(TestLoginPageLogout))
   test_suite.addTest(makeSuite(TestReport))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())