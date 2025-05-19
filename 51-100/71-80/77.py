"""
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
请使用随机模块和列表推导式编写一个程序来输出一个可被5和7整除的随机数,该随机数介于0和10之间。

Hints:
提示：
Use random.choice() to a random element from a list.
对列表中的随机元素使用random.choice()。
"""

# 本人答案
import random
print (random.choice([i for i in range(0,11) if i%5==0 and i%7==0]))