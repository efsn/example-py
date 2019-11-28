# coding:utf-8


import traceback
import ddt
import unittest


testData = [{"username":"tyl","passwd":"123456"},
             {"username":"good","passwd":"123456"},
             {"username":"morning","passwd":"123456"}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print "start"

    def tearDown(self):
        print "end"

    @ddt.data(*testData)
    def test_ddt(self,data):
        print data

if __name__ ==  "__main__":
    unittest.main()

