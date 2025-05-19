"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
使用两个给定的列表[1,3,6,78,35,55]和[12,24,35,24,88,120,155]，编写一个程序来制作一个列表，其元素是上述给定列表的交集。

Hints:
提示：
Use set() and "&=" to do set intersection operation.
使用set()和“&=”执行set交集操作。
"""

# 本人答案
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(intersection([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155]))
