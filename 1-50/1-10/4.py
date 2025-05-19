"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
编写一个程序，从控制台接受逗号分隔的数字序列，并生成一个包含每个数字的列表和元组。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

34,67,55,33,12,98

Then, the output should be:
那么，输出应该是：

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

a=input()
b=tuple(a.split (','))
c=a.split(',')
print(b,c)