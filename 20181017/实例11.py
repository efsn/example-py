# -*- coding: UTF-8 -*-
a=[1,1]
m=int(raw_input("请输入月份："))

if m>1:
    for i in range(1,m):
         a.append(a[i]+a[i-1])
for i in range(a.__len__()):
    if i%6==0:
        print"\n"
    else:
        print a[i],
