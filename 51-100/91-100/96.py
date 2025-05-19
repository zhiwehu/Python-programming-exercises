"""
Please write a program which count and print the numbers of each character in a string input by console.
请编写一个程序，对控制台输入的字符串中的每个字符进行计数和打印。

Example:
例子：
If the following string is given as input to the program:
如果将以下字符串作为程序的输入：

abcdefgabc

Then, the output of the program should be:
那么，程序的输出应该是：

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
提示：

Use dict to store key/value pairs.
使用dict存储键/值对。

Use dict.get() method to lookup a key with default value.
使用dict.get()方法查找具有默认值的键。
"""

# 本人答案
def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
s="abcdefgabc"
print(count_characters(s))