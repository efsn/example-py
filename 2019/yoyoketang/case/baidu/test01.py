#coding:utf-8
from selenium import webdriver
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = u'https://www.baidu.com/'
        self.driver.get(url)
        print "Start!"

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        print  "End!"

    def test01(self):
        u'''测试百度首页，百度一下'''
        result = self.driver.find_element_by_xpath('//input[@type="submit"]').text
        print result
        self.assertEqual(result,u'百度一下')
        print "执行第一个测试用例01"

    def test02(self):
        print "执行第二个测试用例02"

    def test03(self):
        print "执行第三个测试用例03"

if __name__ == " __main__":
    unittest.main()