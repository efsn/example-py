#  coding:utf-8

import unittest


class test01(unittest.TestCase):
    def test(self):
        a = 1+2
        b = 3
        c = self.assertEqual(a,b)
        return c


if __name__ == "__main__":
    a = unittest.test01
    print  a
