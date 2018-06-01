# -*- coding: utf-8 -*-
#提示用户输入一个数字
#电脑随机生成一个数字
#进行比较，并显示结果
import random
playerNum = int(input("请输入一个数字(0：剪刀，1：石头，2：布):"))
computerNum = random.randint(0,2)
print("computerNum = %d" %computerNum)
if(playerNum ==0 and computerNum ==1) or (playerNum ==1 and computerNum ==2) or (playerNum ==2 and computerNum ==0):
    print("你好，你赢了")
elif(playerNum == computerNum):
    print("你好，这是平局")
else:
    print("很不幸，你输了")