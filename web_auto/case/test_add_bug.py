import unittest
from selenium import webdriver
from pages.add_bug_page import AddBugPage
from pages.login_page import LoginPage
import time

class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bug = AddBugPage(cls.driver)
        cls.a=LoginPage(cls.driver)
        cls.a.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = '测试提交bug' + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()


