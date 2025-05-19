"""
Please write a program which accepts a string from console and print it in reverse order.
请编写一个从控制台接受字符串的程序，并按相反顺序打印。

Example:
例子：

If the following string is given as input to the program:
如果将以下字符串作为程序的输入：

rise to vote sir
起立投票，先生

Then, the output of the program should be:
那么，程序的输出应该是：

ris etov ot esir

Hints:
提示：
Use list[::-1] to iterate a list in a reverse order.
使用list[::-1]以相反的顺序迭代列表。
"""

# 本人答案
def reverse_string(s):
    return s[::-1]

s = "rise to vote sir"
print(reverse_string(s))