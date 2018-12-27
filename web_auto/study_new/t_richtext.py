from selenium import webdriver
from pages.login_page import LoginPage
import time

driver=webdriver.Firefox()
a=LoginPage(driver)
a.login()

#打开编辑页面
driver.get("http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html")

#js操作太快了，需要先sleep
time.sleep(3)


editbody='hello xiaolang'
js='document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%editbody

driver.execute_script(js)