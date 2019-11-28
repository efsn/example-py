# -*- coding: UTF-8 -*-
prime=[]


for i in range(0,3):
    a = int(raw_input("输入整数"))
    prime.append(a)

for i in range(0,3):
    for j in range(i,3):
        if prime[i]>prime[j]:
            temp=prime[i]
            prime[i]=prime[j]
            prime[j]=temp


print prime



