# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains



'''   多选框定位方式'''
def abc(driver):
    # 获取链接
    driver.get('https://www.baidu.com/')
    driver.implicitly_wait(10)
    #定位元素，设置
    a= driver.find_element_by_link_text('设置')
    #移动鼠标至“设置按钮”
    ActionChains(driver).move_to_element(a).perform()
    print "移动成功"
    driver.find_element_by_link_text('搜索设置').click()
    #先定位下拉框，再点击选项
    s=driver.find_element_by_xpath('//select[@name="NR"]')
    s.find_element_by_xpath('//option[@value="20"]').click()

    time.sleep(3)
    driver.quit()










#---------------主函数---------------
if __name__ == "__main__":
    driver = webdriver.Chrome()
    abc(driver)











