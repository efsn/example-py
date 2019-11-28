# -*- coding: UTF-8 -*-

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

l=100.00
sum=100.00
for i in range(1,11):
    if(i==1):
        sum=l
    else:
        sum=sum+l*2
    l = l / 2
    print  i,l,sum




