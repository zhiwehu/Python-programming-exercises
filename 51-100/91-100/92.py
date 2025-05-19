"""

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
通过使用列表推导式，请编写一个程序，在删除[12,24,35,24,88,120,155]中的值24后打印列表。

Hints:
提示：
Use list's remove method to delete a value.
使用list的remove方法删除值。
"""

# 本人答案
def remove_value(lst, value):
    return [x for x in lst if x != value]
print(remove_value([12, 24, 35, 24, 88, 120, 155], 24))