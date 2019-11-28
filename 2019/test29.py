#!/usr/bin/python
# -*- coding: UTF-8 -*-

print( '请输入大于10的数字:' )
n=input()
x=[]
i=0;
while(n!=0):
    x.append(n%10)
    i+=1
    n/=10
print( '该数有 %d 位\n' %i )
print( '逆序为：\n')
print( x[::] )