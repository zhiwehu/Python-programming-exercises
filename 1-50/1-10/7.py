"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
编写一个程序,以2位数字X、Y为输入,生成一个二维数组。数组第i行和第j列中的元素值应为i*j。

Example
例子

Suppose the following inputs are given to the program:
假设程序有以下输入：

3,5

Then, the output of the program should be:
那么，程序的输出应该是：

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""

a,b=map(int,input("a,b=").split(','))
c=[]
for i in range(a):
    d=[]
    for j in range(b):
        d.append(i*j)
    c.append(d)        
print(c)