#coding=utf-8
from selenium import webdriver
from common.base import Base
import time

# driver=webdriver.Firefox()
# driver.get('http://127.0.0.1/zentao/user-login.html')
login_url="http://127.0.0.1/zentao/user-login.html"

class LoginPage(Base):
    #定位登陆
    loc_user = ('id', 'account')
    loc_psw = ('css selector', "[name='password']")
    loc_button = ('xpath', './/*[@id="submit"]')
    loc_keep_login=('id','keepLoginon')
    loc_forget_psw=('link text','忘记密码')

    loc_get_user=('css selector','#userMenu>a')

    loc_forget_psw_page=('css selector','.btn')

    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_psw(self,text=""):
        self.sendKeys(self.loc_psw,text)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_loggin(self):
        self.click(self.loc_keep_login)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)

    def login(self,user='admin',psw='123456',keep_login=False):
        '''登陆流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_psw(psw)
        if keep_login:
            self.click_keep_loggin()
        self.click_login_button()

    def get_login_name(self):
        user=self.get_text(self.loc_get_user)
        return user

    def get_login_result(self,text):
        '''返回布尔值'''
        result=self.is_text_in_element(self.loc_get_user,text)
        return result



    def is_refresh_exist(self):
        '''判断忘记密码页面，刷新按钮是否存在'''
        r=self.isElementExist(self.loc_forget_psw_page)
        return r

    def is_alert_exist(self):
        '''判断alert是不是在'''
        a=self.is_alert()
        if a :
            print(a.text)
            a.accept()





if __name__=="__main__":
    driver=webdriver.Firefox()
    login_page=LoginPage(driver)
    login_page.login()
    # driver.get(login_url)
    # login_page.input_user('admin')
    # login_page.input_psw('123456')
    # login_page.click_keep_loggin()
    # login_page.click_login_button()





