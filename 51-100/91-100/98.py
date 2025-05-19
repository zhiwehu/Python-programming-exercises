"""
Please write a program which accepts a string from console and print the characters that have even indexes.
请编写一个从控制台接受字符串的程序，并打印具有偶数索引的字符。

Example:
例子：
If the following string is given as input to the program:
如果将以下字符串作为程序的输入：

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:
那么，程序的输出应该是：

Helloworld
你好世界

Hints:
提示：

Use list[::2] to iterate a list by step 2.
使用list[::2]按步数为2迭代列表。
"""

# 本人答案
def even_index_characters(s):
    return s[::2]
s = "H1e2l3l4o5w6o7r8l9d"
print(even_index_characters(s))