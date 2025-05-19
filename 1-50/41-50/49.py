"""
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
编写一个程序,它可以map()来制作一个列表,其元素是1到20之间的数字的平方(两者都包括在内)。
"""

# 本人答案
def task():
    list1 = range(1, 21)
    list2 = list(map(lambda x: x ** 2, list1))
    print(list2)
task()