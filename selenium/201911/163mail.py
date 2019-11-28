# -*- coding: UTF-8 -*-
from selenium import webdriver
import  time



'''   登录163邮箱'''
def login(driver,user,passwd):
    #获取链接
    driver.get('https://mail.163.com')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="lbNormal"]').click()
    time.sleep(3)
    #切换iframe
    iframe=driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
     #输入用户名
    driver.find_element_by_xpath('//input[@name="email"]').send_keys(user)
    #输入密码
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="dologin"]').click()
    #释放iframe，回到主页面元素
    driver.switch_to_default_content()
    time.sleep(3)

def is_login(driver):
    driver.find_element_by_xpath('//*[@class="Header-item position-relative mr-0 d-none d-lg-flex"]').click()
    time.sleep(2)
    a=driver.find_element_by_xpath('//strong[@class="css-truncate-target"]').text
    print  a
    if a=="elmi-tyl":
     print "登录成功"
    else:
     print "登录失败"
    time.sleep(3)

def logout(driver):
    driver.find_element_by_xpath('//*[@class="dropdown-item dropdown-signout"]').click()
    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    login(driver,'fairy_tyl','720354951989')

    '''
    
    is_login(driver)
    print "hello"
    logout(driver)
    print "goodbye"
    '''









