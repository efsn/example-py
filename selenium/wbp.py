# coding=utf-8
import  time
from selenium import webdriver

driver=webdriver.Chrome()

driver.get('http://192.168.8.29:29062/')  #输入地址栏

driver.find_element_by_xpath("//*[@id='loginId']").send_keys('zhangpd1')  #输入值
driver.find_element_by_xpath("//*[@id='loginPwd']").send_keys('zhangpd')
driver.find_element_by_xpath("//*[@class='loginbg3']/table/tbody/tr").click()  #点击



time.sleep(2)

driver.quit()