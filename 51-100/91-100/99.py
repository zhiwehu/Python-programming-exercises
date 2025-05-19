"""
Please write a program which prints all permutations of [1,2,3]
请编写一个程序，打印[1,2,3]的所有排列


Hints:
提示：
Use itertools.permutations() to get permutations of list.
使用itertools.permutations()来获取列表的排列。
"""

# 本人答案
import itertools
def print_permutations(lst):
    return list(itertools.permutations(lst))
lst = [1, 2, 3]
print(print_permutations(lst))