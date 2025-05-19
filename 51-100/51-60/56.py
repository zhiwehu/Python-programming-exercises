"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
编写一个函数来计算5/0，并使用try/except来捕获异常。

Hints:
提示：

Use try/except to catch exceptions.
使用try/except来捕获异常。
"""
#本人答案
def compute_division():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
compute_division()