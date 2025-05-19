"""
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
编写一个程序来计算1/2+2/3+3/4+。..+n/n+1,控制台输入给定的n(n>0)。

Example:
例子：

If the following n is given as input to the program:
如果将以下n作为程序的输入:

5

Then, the output of the program should be:
那么，程序的输出应该是：

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。

Hints:
提示：
Use float() to convert an integer to a float
使用float()将整数转换为浮点数
"""

# 本人答案
def compute_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i / (i + 1)
    return total

n= int(input("请输入一个正整数n: "))
result = compute_sum(n)