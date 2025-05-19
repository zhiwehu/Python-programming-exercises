"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
对于给定的整数n,编写一个程序来生成一个包含(i,i*i)的字典。该字典是1和n之间的整数(两者都包括在内)然后程序应该打印字典。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

8

Then, the output should be:
那么，输出应该是：

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""

n=int(input("请输入一个数字："))
a={}
for i in range(1,n+1):
    a[i]=i*i
print(a)