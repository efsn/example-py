#!/usr/bin/python
# -*- coding: UTF-8 -*-

L = list(
    filter(
        lambda x: x not in set( [i for i in range(101,201) for j in range(2,i) if not i%j]), range(101,201)
    )
)
print('一共有{}个素数，这些素数分别是：{}'.format(len(L),L))