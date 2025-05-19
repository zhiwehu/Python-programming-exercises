"""
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
编写一个可以filter()的程序,以制作一个元素为1到20之间的偶数(均包含在内)的列表。
"""
# 本人答案
def task():
    list1 = range(1, 21)
    list2 = list(filter(lambda x: x % 2 == 0, list1))
    print(list2)
task()