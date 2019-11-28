# -*- coding: UTF-8 -*-


a=int (raw_input("输入整数"))

while (a!=10):
    if (a>10):
        print "猜大了"
        a = int(raw_input("输入整数"))
    if(a<10):
        print"猜小了"
        a = int(raw_input("输入整数"))
    if(a==10):
        print"猜对了"
        break




