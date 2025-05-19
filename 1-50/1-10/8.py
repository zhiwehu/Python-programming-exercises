"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
编写一个程序，接受逗号分隔的单词序列作为输入，并在按字母顺序排序后以逗号分隔的顺序打印单词。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

without,hello,bag,world


Then, the output should be:
那么，输出应该是：

bag,hello,without,world

"""

str_list=input("输入单词序列(Input word sequence):").split(',')
str_list.sort()
print(','.join(str_list))