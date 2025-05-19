"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
编写一个程序，接受一个句子并计算大写字母和小写字母的数量。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

Hello world!

Then, the output should be:
那么，输出应该是：

UPPER CASE 1
LOWER CASE 9

"""

str1=input("")
a={'UPPER CASE':0 ,'LOWER CASE':0}
for i in str1:
    if i.isupper():
        a['UPPER CASE']+=1
    elif i.islower():
        a['LOWER CASE']+=1
print('UPPER CASE',a['UPPER CASE'])
print('LOWER CASE',a['LOWER CASE'])