"""

Define a class, which have a class parameter and have a same instance parameter.
定义一个类，该类具有类参数和相同的实例参数。

Hints:
提示：
Define a instance parameter, need add it in __init__ method
定义一个实例参数,需要将其添加到__init__方法中

You can init a object with construct parameter or set the value later
您可以使用构造参数初始化对象，也可以稍后设置值
"""
#本人答案
class task ():
    name = " JACK"
    def __init__(self, name,):
        self.name = name


person1=task("JACK")
print(person1.name)

person2=task("MIKE")
print(person2.name)