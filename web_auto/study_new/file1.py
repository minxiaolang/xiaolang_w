#coding=utf-8
from selenium import webdriver
from pykeyboard import PyKeyboard
import time
from pages.login_page import LoginPage
import os

driver=webdriver.Firefox()
a=LoginPage(driver)
a.login()

#打开编辑页面
driver.get("http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html")
time.sleep(2)
driver.find_element_by_css_selector(".ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-image").click()
driver.find_element_by_css_selector(".ke-inline-block.ke-upload-button").click()
time.sleep(12)

k=PyKeyboard()
s="d:\hello.txt"


for i in s:
    k.tap_key(i)
    # print(i)
time.sleep(2)
k.tap_key(k.enter_key)
k.tap_key(k.enter_key)


#发送tab
# k.press_key(k.tab_key)
# k.release_key(k.tab_key)

#回车
# k.tab_key(k.enter_key)

