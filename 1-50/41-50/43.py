"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
编写一个程序来生成并打印另一个元组,其值是给定元组中的偶数(1,2,3,4,5,6,7,8,9,10)。
"""

# 本人答案
def task():
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tuple2 = tuple(i for i in tuple1 if i % 2 == 0)
    print(tuple2)