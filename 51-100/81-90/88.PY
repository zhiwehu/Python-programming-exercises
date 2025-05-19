"""
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
通过使用列表理解，请编写一个程序，在删除[12,24,35,70,88120155]中可被5和7整除的删除数后打印列表。

Hints:
提示：
Use list comprehension to delete a bunch of element from a list.
使用列表理解从列表中删除一堆元素。
"""

# 本人答案
def remove_divisible_by_5_and_7(lst):
    return [x for x in lst if x % 5 != 0 and x % 7 != 0]
print(remove_divisible_by_5_and_7([12, 24, 35, 70, 88, 120, 155]))