# -*- coding: utf-8 -*-
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。 
#程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小
x = input('请输入x=')
y = input('请输入y=')
z = input('请输入z=')
if(x>y):
   t=x
   x=y
   y=t
if(y>z):
   t=y
   z=y
   z=t    
if(z>x):
   t=z
   z=x
   x=t    
print (x,y,z)
   

