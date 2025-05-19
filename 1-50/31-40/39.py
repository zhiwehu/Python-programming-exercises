"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
定义一个函数,该函数可以生成一个列表,其中的值是1到20之间的数字的平方(都包括在内)。然后,该函数需要打印列表中的最后5个元素。
"""

# 本人答案
def task():
    list1 = []
    for i in range(1, 21):
        list1.append(i ** 2)
    print(list1[-5:])