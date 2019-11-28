# -*- coding: UTF-8 -*-
for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print  '%d 等于 %d * %d' %(num,i,j)
            break
    else:
            print '%d 是一个质子' % num


sequence = [12, 34, 34, 23, 45, 76, 89]
for  j in enumerate(sequence):  #使用内置函数进行遍历
    print j


# 输出 2 到 100 简的质数
prime = []   #定义一个列表
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)    #使用内置函数append，作用是在列表末尾添加一个新的对象
print prime






#打印1~9的三角阵列

for k in range(1,11):
       if j<=k:
           print j,
    for j in range(1,k):
    print "\n"






