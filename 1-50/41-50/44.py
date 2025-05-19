"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
编写一个程序,接受字符串作为输入,如果字符串为“YES”、“yes”或“Yes”,则打印“是”;否则打印“否”。
"""

# 本人答案
def task():
    string = input("请输入一个字符串: ")
    if string in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")