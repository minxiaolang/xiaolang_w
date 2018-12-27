from selenium import webdriver
import unittest
from pages.login_page import LoginPage
import time
from pages.add_bug_page import AddBugPage

url="http://127.0.0.1/zentao/user-login.html"
class AddBugCase(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bug=AddBugPage(cls.driver)
        #下面两行cls可以不加，之后用不到
        cls.a=LoginPage(cls.driver)
        cls.a.login()

    def setUp(self):
        '''每个用例都在一个起点开始'''
        self.driver.get(url)

    def test_add_bug(self):
        '''添加bug'''
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = '测试提交bug' + timestr
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()