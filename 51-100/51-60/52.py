"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
定义一个名为Circle的类,它可以由半径构造。Circle类有一个可以计算面积的方法。
"""

# #本人答案
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius ** 2