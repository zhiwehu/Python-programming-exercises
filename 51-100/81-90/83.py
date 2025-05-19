"""
Please write a program to print the running time of execution of "1+1" for 100 times.
请编写一个程序,打印100次“1+1”执行的运行时间。

Hints:
提示：
Use timeit() function to measure the running time.
使用timeit()函数测量运行时间。
"""

# 本人答案
import timeit
def test():
    return 1 + 1
print(timeit.timeit(test, number=100))
