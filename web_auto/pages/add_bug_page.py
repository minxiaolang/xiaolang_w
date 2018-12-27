#coding=utf-8
from selenium import webdriver
from common.base import Base
import time
from pages.login_page import LoginPage


# driver=webdriver.Firefox()
# driver.get('http://127.0.0.1/zentao/user-login.html')

class AddBugPage(Base):
    #定位登陆
    loc1 = ('id', 'account')
    loc2 = ('css selector', "[name='password']")
    loc3 = ('xpath', './/*[@id="submit"]')

    #添加bug
    loc_test=("link text","测试")
    loc_bug=("link text","Bug")
    loc_addbug=("css selector","#createActionMenu>a")
    loc_trunk=("css selector","#openedBuild_chosen>.chosen-choices")
    loc_trunk_add=("css selector",".active-result.highlighted")
    loc_input_title=("id","title")
    #需要先切换iframe
    loc_input_body=("class name","article-content")
    loc_save=("css selector","#submit")

    #新增的列表
    loc_new=('css selector','#bugList>tbody>tr>td:nth-child(4)>a')



    def add_bug(self,title='测试提交bug'):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_trunk)
        self.click(self.loc_trunk_add)
        self.sendKeys(self.loc_input_title,title)
        #输入body
        frame=self.find_element(('class name','ke-edit-iframe'))
        self.driver.switch_to.frame(frame)
        #复文本不能用clear
        # self.clear(self.loc_input_body)
        body='''[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)

if __name__=="__main__":
    driver=webdriver.Firefox()
    bug=AddBugPage(driver)

    a=LoginPage(driver)
    a.login()


    timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
    title='测试提交bug'+timestr
    bug.add_bug(title)
    result=bug.is_add_bug_success(title)
    print(result)




