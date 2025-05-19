"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
编写一个程序，接受行序列作为输入，并在将句子中的所有字符大写后打印行。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

Hello world
Practice makes perfect

Then, the output should be:
那么，输出应该是：

HELLO WORLD
PRACTICE MAKES PERFECT

"""

a=[]
while 1==1:
    s=input()
    if s:
        a.append(s.upper())
    else:
        break
for k in a:
    print(k)