#coding=utf-8
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
'''
1、输入admin,输入13456 点登录 期望结果：
2、输入admin，不输入密码 点登录
3、输入admin，输入admin111，点记住登录按钮，点登陆
'''

testdatas=[{"user":"admin","psw":"123456","expect":"admin"},
           {"user": "admin", "psw": "", "expect": ""},
           {"user": "admin", "psw": "xxxxx", "expect": ""}]
@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self,user,psw,expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        print('测试结果：%s'%result)
        # 断言
        self.assertTrue(result == expect)

    # @ddt.data({"user":"admin","psw":"123456","expect":"admin"},
    #        {"user": "admin", "psw": "", "expect": ""},
    #        {"user": "admin", "psw": "xxxxx", "expect": ""},)
    @ddt.data(*testdatas)
    def test_01(self,data):
        '''输入admin,输入13456 点登录'''
        print('--------------开始测试---------------')
        print('测试数据%s'%data)
        self.login_case(data['user'],data['psw'],data['expect'])
        print('----------------结束----pass----------')


    # def test_02(self):
    #     '''输入admin，不输入密码 点登录'''
    #     print('--------------开始测试2---------------')
    #     data1 = testdatas[1]
    #     print('测试数据%s' % data1)
    #     self.login_case(data1['user'], data1['psw'], data1['expect'])
    #     print('----------------结束----pass----------')
    #
    # def test_03(self):
    #     '''输入admin，输入admin，点记住登录按钮，点登陆'''
    #     print('--------------开始测试3---------------')
    #     data1 = testdatas[2]
    #     print('测试数据%s' % data1)
    #     self.login_case(data1['user'], data1['psw'], data1['expect'])
    #     print('----------------结束----pass----------')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()






