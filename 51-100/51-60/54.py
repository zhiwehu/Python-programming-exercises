"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
定义一个名为Shape的类及其子类Square。Square类有一个init函数，它接受长度作为参数。这两个类都有一个area函数，可以打印默认shape面积为0的形状区域。

Hints:
提示：

To override a method in super class, we can define a method with the same name in the super class.
要覆盖超类中的方法，我们可以在超类中定义一个同名方法。"""
# #本人答案
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2