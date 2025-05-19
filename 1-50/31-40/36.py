"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
定义一个函数,该函数可以生成一个字典,其中键是1到20之间的数字(都包括在内),值是键的平方。该功能应仅打印按键。
"""

# 本人答案
def task():
    dict1 = {}
    for i in range(1, 21):
        dict1[i] = i ** 2
    for key in dict1.keys():
        print(key)