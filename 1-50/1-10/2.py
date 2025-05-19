"""
Write a program which can compute the factorial of a given numbers.
编写一个程序，可以计算给定数字的阶乘。

The results should be printed in a comma-separated sequence on a single line.
结果应以逗号分隔的顺序打印在一行上。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

8

Then, the output should be:
那么，输出应该是：

40320

"""

num=1
n=int(input("请输入一个数字："))
for i in range(1,n+1):
    num=num*i
print(num)