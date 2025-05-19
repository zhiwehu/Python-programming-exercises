"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
编写一个程序,用给定的数字作为a的值来计算a+aa+aaa+aaaa的值。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

9

Then, the output should be:
那么，输出应该是：

11106

"""

num=int(input())
res=num+num*11+num*111+num*1111
print(res)