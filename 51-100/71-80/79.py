"""

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
请编写一个程序,随机生成一个包含5个介于100和200之间的偶数的列表。

Hints:
提示：
Use random.sample() to generate a list of random values.
使用random.sample()生成随机值列表。
"""

# 本人答案
import random
print (random.sample([i for i in range(100,201) if i%2==0],5))