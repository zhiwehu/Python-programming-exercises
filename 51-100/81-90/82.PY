"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
请编写一个程序来压缩和解压缩字符串“hello world!hello world!hello world!hello world!”。

Hints:
提示：
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
使用zlib.compress()和zlib.dexport()来压缩和解压缩字符串。
"""

# 本人答案
import zlib
s = b"hello world!hello world!hello world!hello world!"
s = zlib.compress(s)
print(s)
s = zlib.decompress(s)
print(s)