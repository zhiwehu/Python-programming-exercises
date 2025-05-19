"""
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
请使用生成器编写一个程序,以逗号分隔的形式打印0和n之间可被5和7整除的数字,而n是由控制台输入的。

Example:
例子：

If the following n is given as input to the program:
如果将以下n作为程序的输入:

100

Then, the output of the program should be:
那么，程序的输出应该是：

0,35,70

Hints:
提示：

Use yield to produce the next value in generator.
使用yield在生成器中生成下一个值。

In case of input data being supplied to the question, it should be assumed to be a console input.
如果输入数据被提供给问题，则应假设它是控制台输入。
"""

#本人答案
def task(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
n = int(input("请输入一个整数: "))
task_list = [str(num) for num in task(n)]
print(",".join(task_list))