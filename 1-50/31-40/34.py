"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
定义一个函数,该函数可以打印一个字典,其中键是1到20之间的数字(都包括在内).值是键的平方。

"""

#本人答案
def print_square_dict():
    square_dict = {i: i**2 for i in range(1, 21)}
    for key, value in square_dict.items():
        print(f"{key}: {value}")

print_square_dict()