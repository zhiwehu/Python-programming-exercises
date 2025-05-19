"""
Question 71:
问题：

Please write a program which accepts basic mathematic expression from console and print the evaluation result.
请编写一个程序，从控制台接受基本的数学表达式，并打印评估结果。

Example:
例子：

If the following string is given as input to the program:
如果将以下字符串作为程序的输入：

35+3

Then, the output of the program should be:
那么，程序的输出应该是：

38

Hints:
提示：
Use eval() to evaluate an expression.
使用eval()来计算表达式。
"""

# 本人答案
s=eval(input("请输入一个数学表达式: "))
print(s)