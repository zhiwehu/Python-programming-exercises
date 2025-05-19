"""
write a program that accepts a sentence and calculate the number of letters and digits.
编写一个程序，接受一个句子并计算字母和数字的数量。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

hello world! 123

Then, the output should be:
那么，输出应该是：

LETTERS 10
DIGITS 3
"""

str1=input()
a={'LETTERS':0 ,'DIGITS':0}
for i in str1:
    if i.isalpha():
        a['LETTERS']+=1
    elif i.isdigit():
        a['DIGITS']+=1
print('LETTERS',a['LETTERS'])
print('DIGITS',a['DIGITS'])