#coding:utf-8
from selenium import webdriver
import time



def login(driver,user,passwd):
    driver.get(u'https://account.cnblogs.com/signin')
    driver.find_element_by_name('LoginName').send_keys(user)
    driver.find_element_by_name('Password').send_keys(passwd)
    time.sleep(2)
    driver.find_element_by_xpath('//span[@class="ladda-label"]').click()
    cookie = driver.get_cookies()
    time.sleep(2)
    print  cookie
    time.sleep(3)
    a = driver.find_element_by_xpath('//*[@id="header_user_right"]/a[2]').text
    print "获取到我的用户名：", a
    if a == "elmi":
        print "登陆成功"
        return True
    else:
        print "登陆失败"
        return False

def login_out(driver):
    driver.find_element_by_xpath('//*[@id="header_user_right"]/a[5]').click()
    driver.quit()




if __name__ ==  "__main__":
    driver=webdriver.Chrome()
    login(driver,"elmi","yltang*mail123")
    login_out(driver)