# -*- coding: UTF-8 -*-

import random
while(1):
    m=int(random.randint(1, 3))
    if(m==1):
        com='石头'
    elif(m==2):
        com='剪刀'
    else:
        com='布'
    you=raw_input("请输入石头、剪刀、布猜拳，输入end，游戏结束")
    blist=['石头','剪刀','布']
    if  (you!='end')and (you not in blist):
       print "输入有误，请重新输入"
    elif(you=='end'):
        print "游戏结束..."
        break
    elif(you=='石头'and com=='剪刀')or(you=='剪刀'and com=='布')or(you=='布'and com=='石头'):
        print "电脑出的是:"+com+",你赢了"
    elif(com=='石头'and you=='剪刀')or(com=='剪刀'and you=='布')or(com=='布'and you=='石头'):
        print "电脑出的是:"+com+",你输了"
    elif(com==you):
        print"电脑出的是:"+com+",最终结果是平局"




