#coding=utf-8
from selenium import webdriver
import time
import unittest
#导入测试框架

class LoginTest(unittest.TestCase):
    '''登陆类的案例'''
    #driver----self.driver:局部变量-----全局变量
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        url = 'http://127.0.0.1/zentao/user-login.html'
        self.driver.get(url)

    # def tearDown(self):
    #     self.driver.delete_all_cookies()  #清空cookies
    #     self.driver.refresh()

    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector('#userMenu>a').text
            # print(t)
            return t
        except:
            return ''

    def is_alert_exist(self):
        '''判断slert是不是在'''
        try:
            time.sleep(2)
            alert=self.driver.switch_to.alert()
            text=alert.text
            alert.accept()
            return text
        except:
            return ''

    def login(self,user,pwd):
        self.driver.find_element_by_id('account').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_id('submit').click()


    def test_01(self):
        '''正确的登录'''
        time.sleep(2)

        self.login('admin','123456')

        # self.driver.find_element_by_id('account').send_keys('admin')
        # self.driver.find_element_by_name('password').send_keys('123456')
        # self.driver.find_element_by_id('submit').click()

        #判断是否登录成功
        time.sleep(2)
        t=self.get_login_username()
        print('获取的结果：%s'%t)
        self.assertTrue(t=='admin')
    #
    def test_02(self):
        '''错误的登录'''
        time.sleep(2)

        self.login('admin1','1234')

        # self.driver.find_element_by_id('account').send_keys('admin11')
        # self.driver.find_element_by_name('password').send_keys('1234516')
        # self.driver.find_element_by_id('submit').click()

        # 判断是否登录成功
        time.sleep(2)
        t = self.get_login_username()
        print('登录失败，获取结果:%s'%t)
        self.assertTrue(t == '')  #断言失败

    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
