# -*- coding: UTF-8 -*-
#打印等腰直接三角形
rows = int(raw_input('输入列数： '))
print"等腰直接三角形1"
for i in range(0,rows):
    for j in range(0,rows):
        if (i+j<rows):
            print " * ",
    print "\n"


#打印等腰直接三角形
rows = int(raw_input('输入列数： '))
print"等腰直接三角形2"
for i in range(0,rows):
    for i in range(0, rows-i):
        print " * ",
    print "\n"

#打印实心正方形
rows = int(raw_input('输入列数： '))
print"实心正方形"
for i in range(0,rows):
    for j in range(0, rows):
        print" * ",
    print"\n"
#打印空心正方形
rows = int(raw_input('输入列数： '))
print"空心正方形"
for i in range(0,rows):
    for j in range(0, rows):
        if(i==0)or(i==rows-1):
            print" * ",
        else:
            if(j==0)or(j==rows-1):
                print " * ",
            else:
                print"   ",
    print"\n"

#打印实心三角形
rows = int(raw_input('输入列数： '))
print"实心三角形"
for i in range(0,rows):
    for j in range(0,rows-i):
        print " ",

    for k in range(0,2*rows-1):
        if(k%2==0):
            print"*",
        else:
            print" ",
    print "\n"



