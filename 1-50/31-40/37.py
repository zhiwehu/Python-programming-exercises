"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
定义一个函数,该函数可以生成并打印一个列表,其中的值是1到20之间的数字的平方(均包括在内)。
"""

# 本人答案
def task():
    list1 = []
    for i in range(1, 21):
        list1.append(i ** 2)
    print(list1)