## -*- coding: utf-8 -*-
# 题目：判断101-200之间有多少个素数，并输出所有素数。
#算法思路：
#1、取101-200中所有的整数
#2、判断该数是否为素数：该数除以（2到sqrt中的数）如果余数不为0，则说明为素数
#3、输出所有素数，和个数总数
h = 0
p = 0
from math import sqrt
from sys import stdout
for m in range(101,201): #左开右闭
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            p =1
            break
    if p == 0:
        print ('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    p = 0
print ('The total is %d' % h)
