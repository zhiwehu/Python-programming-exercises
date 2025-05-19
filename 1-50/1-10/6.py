"""
Write a program that calculates and prints the value according to the given formula:
编写一个程序，根据给定的公式计算并打印值：

Q = Square root of [(2 * C * D)/H]
Q=[(2*C*D)/H]**0.5

Following are the fixed values of C and H:
以下是C和H的固定值,

C is 50. H is 30.
C是50。H是30。

D is the variable whose values should be input to your program in a comma-separated sequence.
D是变量,其值应以逗号分隔的顺序输入到程序中。

Example
例子

Let us assume the following comma separated input sequence is given to the program:
让我们假设程序有以下逗号分隔的输入序列：

100,150,180

The output of the program should be:
程序的输出应该是：

18,22,24

Hints:
提示：
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
如果接收到的输出是十进制形式的,则应四舍五入到最接近的值(例如,如果收到的输出是26.0,则应打印为26)

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。
"""

def task(d):
    c=50
    h=30
    q=int(((2*c*d)/h)**0.5)
    return q

a=list((input("输入数字").split(",")))
for i in a:
    print(task(int(i)),end=",")
