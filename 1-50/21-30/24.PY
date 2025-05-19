"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Python有很多内置函数,如果你不知道如何使用它,你可以在线阅读文档或找一些书。但是Python对每个内置函数都有一个内置的文档函数。

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
请编写一个程序来打印一些Python内置函数文档,如abs()、int()、input()

And add document for your own function
同时为您自己的功能添加文档
"""


#本人答案
help(abs)
help(int)
help(input)

def square(num):
    '''返回输入数字的平方值。
    
    输入数字必须是整数。
    '''
    return num ** 2
