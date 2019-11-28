# -*- coding: UTF-8 -*-
#斐波那契数列
n=int(raw_input("输入整数"))
a=[0,1]

def abc (i):
    c=a[i-1]+a[i]
    a.append(c)
    return a

for i in range(1,n):
    abc(i);
print a