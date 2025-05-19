"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
编写一个程序,接受逗号分隔的4位二进制数序列作为输入,然后检查它们是否能被5整除。可被5整除的数字将以逗号分隔的顺序打印。

Example:
例子：

0100,0011,1010,1001

Then the output should be:
那么输出应该是：

1010

Notes: Assume the data is input by console.
注：假设数据是通过控制台输入的。

"""

a=input().split(",")
c=[]
for i in a:
    b=int(i,2)
    if b%5==0:
        c.append(i)
print(','.join(c))