"""
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
您需要编写一个程序,按升序对(name、age、height)元组进行排序,其中name是字符串,age和height是数字。元组由控制台输入。排序标准为：

1: Sort based on name;
1:按名称排序；

2: Then sort based on age;
2:然后按年龄排序；

3: Then sort by score.
3:然后按分数排序。

The priority is that name > age > score.
优先顺序是姓名>年龄>分数。

If the following tuples are given as input to the program:
如果将以下元组作为程序的输入：

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:
那么，程序的输出应该是：

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
提示：

We use itemgetter to enable multiple sort keys.
我们使用itemgetter来启用多个排序键。
"""

#本人答案
list1=[]
while True:
    s=input()
    if not s:
        break
    tup=tuple(s.split(','))
    list1.append(tup)
list1.sort(key=lambda x: (x[0], int(x[1]),int(x[2])))
print(list1)