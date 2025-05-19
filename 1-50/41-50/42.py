"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
对于给定的元组(1,2,3,4,5,6,7,8,9,10),编写一个程序,将前半部分值打印在一行中,将后半部分值打印到一行中。
"""

# 本人答案
def task():
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tuple1[:5])
    print(tuple1[5:]) 