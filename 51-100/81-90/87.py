"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
请编写一个程序，在删除[5,6,77,45,22,12,24]中的删除偶数后打印列表。

Hints:
提示：
Use list comprehension to delete a bunch of element from a list.
使用列表理解从列表中删除一堆元素。
"""

# 本人答案
def remove_even_numbers(lst):
    return [x for x in lst if x % 2 != 0]
print(remove_even_numbers([5, 6, 77, 45, 22, 12, 24]))