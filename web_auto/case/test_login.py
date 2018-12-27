#coding=utf-8
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
'''
1、输入admin,输入13456 点登录 期望结果：
2、输入admin，不输入密码 点登录
3、输入admin，输入admin，点记住登录按钮，点登陆
4、点忘记密码
'''
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入admin,输入13456 点登录'''
        self.loginp.input_user('admin')
        self.loginp.input_psw('123456')
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        #断言
        self.assertTrue(result=='admin')

    def test_02(self):
        '''输入admin，不输入密码 点登录'''
        self.loginp.input_user('admin')
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == '')

    def test_03(self):
        '''输入admin，输入admin，点记住登录按钮，点登陆'''
        self.loginp.input_user('admin')
        self.loginp.input_psw('123456')
        self.loginp.click_keep_loggin()
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == 'admin')

    def test_04(self):
        '''点忘记密码,刷新按钮是否存在'''
        self.loginp.click_forget_psw()
        #断言
        result=self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()






