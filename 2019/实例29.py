# -*- coding: UTF-8 -*-

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

a=input('输入一个不多于5位的正整数')

l=[]
j=0   #位数

for i in range(1,6):
    if a==0:
        break
    else:
        l.append(a%10)
        a=a/10
        j=j+1

print '逆序为',l[:],'\n数据长度为',j
