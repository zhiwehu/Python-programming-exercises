"""

Please write a program to shuffle and print the list [3,6,7,8].
请编写一个程序来洗牌并打印列表[3,6,7,8]。

Hints:
提示：
Use shuffle() function to shuffle a list.
使用shuffle()函数对列表进行洗牌。
"""

# 本人答案
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([3, 6, 7, 8]))