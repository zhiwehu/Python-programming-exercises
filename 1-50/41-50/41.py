"""
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
定义一个函数,该函数可以生成并打印一个元组,其中值是1到20之间的数字的平方(都包括在内)。
"""

# 本人答案
def task():
    tuple1 = tuple(i ** 2 for i in range(1, 21))
    print(tuple1)