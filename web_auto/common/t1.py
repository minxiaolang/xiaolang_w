from selenium import webdriver
import time


driver=webdriver.Firefox()
driver.get('http://nj.ganji.com/')

time.sleep(5)
#滚动底部，第一个0代表横向滚动条在最左边
js="window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)

time.sleep(5)
#回到顶部
js="window.scrollTo(0,0)"
driver.execute_script(js)

#滚动到元素出现的位置
ele=driver.find_element_by_link_text("二手市场")
driver.execute_script("arguments[0].scrollIntoView();",ele)

