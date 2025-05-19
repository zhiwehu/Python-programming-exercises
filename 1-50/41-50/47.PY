"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
编写一个可以map()和filter()的程序,以制作一个元素为[1,2,3,4,5,6,7,8,9,10]中偶数平方的列表。
"""
# 本人答案
def task():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list1)))
    print(list2)

task()