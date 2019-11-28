# coding=utf-8
import time
from selenium import webdriver

browser = webdriver.Chrome()

# 使用get方法请求百度网页
browser.get('https://www.baidu.com')
# page_source属性用于获取网页的源代码，然后就可以使用正则表达式，css，xpath，bs4来解析网页
print(browser.page_source)
browser.close()