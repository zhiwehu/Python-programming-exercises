"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
定义一个函数，该函数可以接受两个字符串作为输入，并在控制台中打印具有最大长度的字符串。如果两个字符串的长度相同，则函数应逐行打印所有字符串。
"""

#本人答案
def task(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        return str1 + "\n" + str2
    
str1 = "Hello"
str2 = "World!"
print(task(str1, str2))