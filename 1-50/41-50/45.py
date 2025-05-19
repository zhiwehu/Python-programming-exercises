"""
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
编写一个程序，通过使用过滤函数过滤列表中的偶数。列表为：[1,2,3,4,5,6,7,8,9,10]。
"""

# 本人答案
def task():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list(filter(lambda x: x % 2 == 0, list1))
    print(list2)