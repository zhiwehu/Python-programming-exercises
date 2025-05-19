"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
对于给定的列表[12,24,35,24,88,120,155,88,120,155]，在保留原始顺序的情况下删除所有重复值后，编写一个程序打印此列表。

Hints:
提示：
Use set() to store a number of values without duplicate.
使用set()存储多个不重复的值。
"""

# 本人答案
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result    
    
print(remove_duplicates([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]))