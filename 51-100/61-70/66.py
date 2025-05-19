"""
The Fibonacci Sequence is computed based on the following formula:
斐波那契数列根据以下公式计算：


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.
请编写一个程序,通过控制台输入给定的n来计算f(n)的值。

Example:
例子：

If the following n is given as input to the program:
如果将以下n作为程序的输入:

7

Then, the output of the program should be:
那么，程序的输出应该是：

13

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。

Hints:
提示：
We can define recursive function in Python.
我们可以在Python中定义递归函数。
"""

# 本人答案
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("请输入一个非负整数n: "))
result = fibonacci(n)
print(f"f({n}) = {result}")