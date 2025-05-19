"""
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
编写一个可以映射（）的程序来制作一个列表，该列表的元素是[1,2,3,4,5,6,7,8,9,10]中元素的平方。
"""

# 本人答案
def task():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list(map(lambda x: x ** 2, list1))
    print(list2)

task()