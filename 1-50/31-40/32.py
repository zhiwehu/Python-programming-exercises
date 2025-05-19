"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
定义一个可以接受整数作为输入的函数，如果该数字是偶数，则打印“它是偶数”，否则打印“这是奇数”。
"""

#本人答案
def task(num):
    if num % 2 == 0:
        return "It is an even number\n这是偶数"
    else:
        return "It is an odd number\n这是奇数"
    
num = 10
print(task(num))