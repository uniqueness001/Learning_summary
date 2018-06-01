# -*- coding: utf-8 -*-
#定义一个列表，存放所要分配的元素
#定义一个列表，嵌套多个分配列表
#随机分配到各个列表中
import random
teachers =['A','B','C','D','E','F','G','H']
rooms =[[],[],[]] #左右都开
for name in teachers:
    randomNum = random.randint(0, 2)
    rooms[randomNum].append(name)

s=1
for room in rooms:
    print("办公室%d里面的老师是:" % s)
    for name in room:
        print(name,end =" ")
    print("")
    s+=1

