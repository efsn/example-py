# -*- coding: UTF-8 -*-
#d打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if(j<=i):
            m=i*j
            print "%d*%d =%d " %(j,i,m),
    print"\n"
