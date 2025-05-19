"""
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
请使用随机模块和列表理解编写一个程序,输出0到10之间的随机偶数。

Hints:
提示：

Use random.choice() to a random element from a list.
对列表中的随机元素使用random.choice()。
"""

#本人答案
import random
print (random.choice([i for i in range(0,11) if i%2==0]))
