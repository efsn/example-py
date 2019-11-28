# -*- coding: UTF-8 -*-

#求1+2!+3!+...+20!的和。


def sum(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    return  s

t=0
for j in range(1,21):
    t=t+sum(j)


print t





print '5!的值为',d