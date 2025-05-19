"""
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
编写一个程序来计算输入中单词的频率。输出应在按字母数字对键进行排序后输出。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Python新手还是在Python 2和Python 3之间做出选择?阅读Python 2或Python 3。

Then, the output should be:
那么，输出应该是：

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""

#本人答案
while True:
    s=input()
    if not s:
        break
    s = s.split()
    dict1={}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    dict1 = sorted(dict1.items())
    print(dict1)