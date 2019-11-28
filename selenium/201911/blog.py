# -*- coding: UTF-8 -*-
from selenium import webdriver
import  time


#登陆博客页
def login(driver):
    driver.find_element_by_id("blog_nav_newpost").click()
    time.sleep(3)
    driver.find_element_by_name('LoginName').send_keys('')
    driver.find_element_by_name('Password').send_keys('')
    driver.find_element_by_xpath('//span[@class="ladda-label"]').click()
    time.sleep(2)


def edit(driver):
    title=u'selenium_test'
    driver.find_element_by_xpath('//*[@formcontrolname="title"]').send_keys(title)
    body=u'34920'
    driver.switch_to_frame('Editor_Edit_EditorBody_ifr')
    driver.find_element_by_xpath('//*[@id="Editor_Edit_EditorBody_ifr"]').send_keys(body)
    time.sleep(3)




if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = r'https://i-beta.cnblogs.com/posts/edit'
    driver.get(url)
    edit(driver)
    driver.quit()