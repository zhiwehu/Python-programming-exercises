"""
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
通过使用列表理解，请编写一个程序，在删除[12,24,35,70,88120155]中的第0、第4、第5个数字后打印列表。

Hints:
提示：
Use list comprehension to delete a bunch of element from a list.
使用列表推导式从列表中删除一堆元素。

Use enumerate() to get (index, value) tuple.
使用enumerate()来获取(索引，值)元组。
"""

# 本人答案
def remove_indices(lst, indices):
    return [x for i, x in enumerate(lst) if i not in indices]
print(remove_indices([12, 24, 35, 70, 88, 120, 155], {0, 4, 5}))
