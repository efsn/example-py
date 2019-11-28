# -*- coding: UTF-8 -*-

#利用递归方法求5!。

def jiecheng(m):
    if m==1:
        s=1
    else:
        s=jiecheng(m-1)*m
    return  s


print '5!的值为',jiecheng(5)
