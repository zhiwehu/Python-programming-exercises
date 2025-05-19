"""
The Fibonacci Sequence is computed based on the following formula:
斐波那契数列根据以下公式计算：


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
请编写一个使用列表推导式的程序,通过控制台输入给定的n,以逗号分隔的形式打印斐波那契序列。

Example:
例子：
If the following n is given as input to the program:
如果将以下n作为程序的输入:

7

Then, the output of the program should be:
那么，程序的输出应该是：

0,1,1,2,3,5,8,13

Hints:
提示：
We can define recursive function in Python.
我们可以在Python中定义递归函数。
Use list comprehension to generate a list from an existing list.
使用列表推导式从现有列表生成列表。
Use string.join() to join a list of strings.
使用string.join()连接字符串列表。

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。
"""

# 本人答案
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("请输入一个整数: "))
fibonacci_list = [str(fibonacci(i)) for i in range(n + 1)]