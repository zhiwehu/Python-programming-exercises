"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
编写一个程序,接受一系列空格分隔的单词作为输入,并在删除所有重复单词并按字典序排序后打印单词。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

hello world and practice makes perfect and hello world again
你好世界，熟能生巧，再次你好世界

Then, the output should be:
那么,输出应该是：

again and hello makes perfect practice world
再次,hello创造了完美的实践世界

Hints:
提示：

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。

We use set container to remove duplicated data automatically and then use sorted() to sort the data.
我们使用set容器自动删除重复的数据,然后使用sorted()对数据进行排序。
"""

a=list(set(input().split(" ")))
a.sort()
print(' '.join(a))

"""
sorted会创造一个新的列表,并返回一个新的列表,而不是在原地排序
sort在原来的列表进行排序,并返回None

Sorted will create a new list and return a new list instead of sorting in place
Sort sorts the original list and returns None

sorted可对任何可以排序的数据结构进行排序,包括列表、元组、字符串等
sort只能对列表进行排序

Sorted can sort any data structure that can be sorted, including lists, tuples, strings, etc
Sort can only sort a list
"""