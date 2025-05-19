"""
Question 21
问题21
Level 3
级别3

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
机器人从原点(0,0)开始在平面内移动。机器人可以按照给定的步骤向上、向下、向左和向右移动。机器人运动轨迹如下:
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
方向后面的数字是步数。请编写一个程序来计算一系列移动和原点后与当前位置的距离。如果距离是浮点数，则只需打印最接近的整数。

Example:
例子：

If the following tuples are given as input to the program:
如果将以下元组作为程序的输入：

UP 5
DOWN 3
LEFT 3
RIGHT 2

Then, the output of the program should be:
那么，程序的输出应该是：

2
"""
#本人答案
location=[0,0]
while True:
    s=input()
    if not s:
        break
    ss=s.split()
    if ss[0] == 'UP':
        location[1] += int(ss[1])
    elif ss[0] == 'DOWN':
        location[1] -= int(ss[1])
    elif ss[0] == 'LEFT':
        location[0] -= int(ss[1])
    elif ss[0] == 'RIGHT':
        location[0] += int(ss[1])
print(int((location[0]**2+location[1]**2)**0.5))