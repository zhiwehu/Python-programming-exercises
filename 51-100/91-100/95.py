"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
定义一个类Person及其两个子类:男性和女性。所有类都有一个方法“getGender”,可以为男性类打印“Male”,为女性类打印“Female”。

Hints:
提示：
Use Subclass(Parentclass) to define a child class.
使用子类（父类）定义子类。
"""
# 本人答案
class Person:
    def getGender(self):
        pass
class male(Person):
    def getGender(self):
        print("Male")
class female(Person):
    def getGender(self):
        print("Female")