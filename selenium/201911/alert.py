# -*- coding: UTF-8 -*-
from selenium import webdriver
import  time

def alert(driver):
    driver.find_element_by_xpath('//input[@id="alert"]').click()
    print '123'
    time.sleep(2)
    #切换到警告窗口
    t = driver.switch_to_alert()
    #打印警告文本框的内容
    print t.text
    #点击警告框的确认按钮
    t.accept()
    print "确定成功"
    #点击警告框的取消按钮，相当于点X
    #t.dismiss()
    #print "关闭成功"

def confirm(driver):
    driver.find_element_by_xpath('//input[@id="confirm"]').click()
    print '123'
    time.sleep(2)
    t = driver.switch_to_alert()
    t.accept()
    print "确定成功"



def prompt(driver):
    driver.find_element_by_xpath('//input[@id="prompt"]').click()
    print '123'
    time.sleep(2)
    t = driver.switch_to_alert()
    print t.text
    #输入框输入文本，此时无效？？？
    t.send_keys('hello world')
    time.sleep(2)
    t.accept()
    print "确定成功"

def radio(driver):
    driver.find_element_by_xpath('//input[@id="girl"]').click()
    print "girl"
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="boy"]').click()
    print "boy"
    time.sleep(2)

def checkbox(driver):
    #选择一组元素，注意需要加复数driver.find_elements_by_xpath
    checkboxs = driver.find_elements_by_xpath('//*[@type="checkbox"]')
    for i in checkboxs:
        #判断是否被选中。如果被选中，跳出循环，没有选中，再点击。
        a=i.is_selected()
        if a=="true":
            break;
        else:
            i.click()
            time.sleep(1)







if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = r'E:\python\test_book\test_alert.html'
    driver.get(url)
    alert(driver)
    confirm(driver)
    prompt(driver)

    url=(r'E:\python\test_book\radio.html')
    driver.get(url)
    radio(driver)
    checkbox(driver)

    driver.quit()












