#coding:utf-8
from selenium import webdriver
import  time


#判断元素查找是否正确


def is_element(driver):
    #s = driver.find_element_by_xpath('//input[@type="submit"]')
    d= driver.find_element_by_css_selector()
    if len(s) == 0:
        print "元素不存在"
        return False
    elif len(s) == 1:
        print  "元素查找准确"
        print s.text
        return True
    else:
        print "元素存在多个"
        return False

    time.sleep(2)
    quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = u'https://www.baidu.com/'
    driver.get(url)
    s=driver.find_element_by_xpath('//input[@class="btn self-btn bg s_btn"]')

    print (s.get_attribute(value))

