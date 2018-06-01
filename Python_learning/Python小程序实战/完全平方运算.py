# -*- coding: utf-8 -*-
#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
#程序分析：循环计算即可，判断成立即可输出。首先要判断是否为正整数。引入math模块算平方根。
import math
for i in range(10000):
    for j in range(10000):
        if(i*i-j*j==168 and i*i-268>0):
            print(i,j)
            print("该数为：%d"%(i*i-268))
                        
            

