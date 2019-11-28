# -*- coding: UTF-8 -*-

#打印实心的三角形
rows=int(raw_input("输入整数："))
for i in range(0,rows):
    for j in range(0,rows-i):
        print " ",
    for k in range(0,i+1):
        print " * ",
    print "\n"

# 打印空心的三角形
rows=int(raw_input("输入整数："))
for i in range(0,rows):
    for j in range(0,rows-i):
        print " ",
    for k in range(0,i+1):
        if k==0 or i==rows-1  or k==i :
            print " * ",
        else:
            print "   ",
    print "\n"


#打印空心等边三角形
rows=int(raw_input("输入整数："))
for i in range(0,rows):
    for j in range(0,2*rows-1):
        if i==rows-1:
            if (j%2==0):
                print " * ",
            else:
                print "   ",

        else:
            if j==rows-i-1 or j==rows+i-1:
                print " * ",
            else:
                print "   ",

    print"\n"


