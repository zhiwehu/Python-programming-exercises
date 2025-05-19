"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
使用生成器定义一个类,该生成器可以迭代给定范围0和n之间的可被7整除的数字。
"""

#本人答案
class task():
    def find(self,n):
        for i in range(1, n+1):
            if i % 7 == 0:
                print(i,end=',')
            
num=int(input())
task1=task()
task1.find(num)
