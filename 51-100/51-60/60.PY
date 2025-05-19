"""
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
编写一个程序，接受由空格分隔的单词序列作为输入，打印仅由数字组成的单词。

Example:
例子：

If the following words is given as input to the program:
如果将以下单词作为程序的输入：

2 cats and 3 dogs.

Then, the output of the program should be:
那么，程序的输出应该是：

2 3

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。
"""

#本人答案
input_str = input("请输入由空格分隔的单词序列：")
words = input_str.split()
result = [word for word in words if word.isdigit()]
print(" ".join(result))
