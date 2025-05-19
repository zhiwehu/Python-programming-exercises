"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
使用列表推导式法将列表中的每个奇数平方。列表由逗号分隔的数字序列输入。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

1,2,3,4,5,6,7,8,9

Then, the output should be:
那么，输出应该是：

1,3,5,7,9

我的老师告诉我使用列表推导式或许可以使代码变得更加简洁,但是一个好的代码追求的应该让人可以读得懂,而不是最少的行数。
My teacher told me that using list dcomprehension may make the code more concise, but good code should strive for readability, not the minimum number of lines.
"""

#使用列表推导式
a = [i for i in input().split(',') if int(i) % 2 != 0]
print(','.join(a))


#不使用列表推导式
a=input().split(',')
b=[]
for i in a:
    if int(i)%2!=0:
        b.append(i)
print(','.join(b))