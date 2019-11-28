# -*- coding: UTF-8 -*-

#判断101~200之间有多少素数，并输出所有的素数
a=[]
for i in range(101,200):
    for j in range(2,i):
        if i%j==0:
            break;
    else:
            print i,
            a.append(i)

print"\n素数的个数为",a.__len__()





