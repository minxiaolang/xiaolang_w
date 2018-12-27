from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base(object):

    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=10
        self.t=0.5

    def find_element(self, locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc=("od","value")')
        else:
            print('正在定位元素信息，定位方式-->%s,value值-->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElementNew(self,locator):
        '''定位到元素返回元素对象，没有定位到就返回timeout异常'''
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def isElementExist(self,locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        eles=self.find_elements(locator)
        n=len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print('定位到多个元素的个数：%s '%n)
            return True

    def find_elements(self,loctor):
        try:
            eles= WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*loctor))
            return eles
        except:
            return []

    def sendKeys(self,loctor,text):
        ele=self.find_element(loctor)
        ele.send_keys(text)

    def click(self,loctor):
        ele=self.find_element(loctor)
        ele.click()

    def clear(self,loctor):
        ele=self.find_element(loctor)
        ele.clear()

    def isSelected(self,loctor):
        '''判断元素是否被选中，返回bool值'''
        ele=self.find_element(loctor)
        r=ele.is_selected()
        return r

    def is_title(self,_title):
        '''返回bool值'''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        '''返回bool值'''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''返回bool值'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc=("od","value")')
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''返回bool值，value为空字符串，返回false'''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result=WebDriverWait(self.driver,3,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self,locator):
        '''获取文本'''
        try:
            t=self.find_element(locator).text
            return t
        except:
            print("获取文本失败，返回'' ")
            return ''

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele=self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选择第一个'''
        ele=self.find_element(locator)
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        ele=self.find_element(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本值定位'''
        ele=self.find_element(locator)
        Select(ele).select_by_visible_text(text)

    def js_focus_element(self,locator):
        '''聚焦元素，滚动条滚到那边'''
        target=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_end(self):
        '''滚动到底部'''
        js="window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)






if __name__=='__main__':
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1/zentao/user-login.html')
    zentao=Base(driver)
    loc1 = (By.ID, 'account')
    #loc1=('id','axxount')  #这样写可以不导入By
    loc2 = (By.NAME, 'password')
    #loc2=('css_selector',"name='[password]'")
    #loc2=('name','password')
    loc3 = (By.ID, 'submit')
    zentao.sendKeys(loc1,'admin')
    zentao.sendKeys(loc2,'123456')
    zentao.click(loc3)

