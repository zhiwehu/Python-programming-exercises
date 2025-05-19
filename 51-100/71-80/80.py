"""
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
请编写一个程序,随机生成一个包含5个数字的列表,这些数字可以被5和7整除,介于1和1000之间。

Hints:
提示：
Use random.sample() to generate a list of random values.
使用random.sample()生成随机值列表。
"""
# 本人答案
import random
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))