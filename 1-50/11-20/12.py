"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
编写一个程序,它将找到1000到3000之间的所有的每一位都是偶数的数字(包括1000和3000)。

The numbers obtained should be printed in a comma-separated sequence on a single line.
获得的数字应以逗号分隔的顺序打印在一行上。

Hints:
提示：

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。

"""

num=[]
for i in range(1000,3001):
    a=i
    while a>0:
        b=a%10
        a//=10
        if b%2!=0:
            break
    else:
        num.append(str(i))
print(','.join(num))