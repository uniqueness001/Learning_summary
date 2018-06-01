# -*- coding: utf-8 -*-
#1、存在有很多名字的列表
#2、输入想要查询的名字
#3、判断是否存在，并显示相应提示
names =['张富民','杨碌荣','余梓煜','彭国鑫']
insertname = input("请输入你要查询的名字：")
findflag =0
for name in names:
    if name == insertname:
        findflag = 1
        break #如果在前面已经找到了需要的名字，那么就结束循环，退出 findflag = 1
if(findflag ==1):
    print("找到了")
else:
    print("没有找到")
    names.append(insertname)
    names.insert(1,insertname)
print(names)