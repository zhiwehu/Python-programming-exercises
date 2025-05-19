"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
编写一个程序,找出所有能被7整除但不是5的倍数的数字,

between 2000 and 3200 (both included).
2000至3200(均包括在内)。

The numbers obtained should be printed in a comma-separated sequence on a single line.
获得的数字应以逗号分隔的顺序打印在一行上。

"""

for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')
         