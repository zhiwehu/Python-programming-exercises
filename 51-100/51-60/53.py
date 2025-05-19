"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
定义一个名为Rectangle的类,它可以由长度和宽度构造。Rectangle类有一个可以计算面积的方法。

Hints:
提示：

Use def methodName(self) to define a method.
使用def methodName（self）定义方法。
"""
#本人答案
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width