
# -*- coding: UTF-8 -*-
import  time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.12306.cn/index/index.html')

a=driver.find_element_by_link_text("中国铁路12306")#通过链接文本寻找元素
time.sleep(5)
driver.get_screenshot_as_file(r'E:\test\a.jpg')#  获取截图

#  获取元素标签的内容
text1=a.get_attribute('textContent')
text2=a.text

print text1





time.sleep(1)

driver.quit()
