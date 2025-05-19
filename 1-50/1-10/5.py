"""
Define a class which has at least two methods:
定义一个至少有两个方法的类：

getString: to get a string from console input
getString:从控制台输入中获取字符串

printString: to print the string in upper case.
printString:打印大写字符串。

Also please include simple test function to test the class methods.
另外，请包含简单的测试函数来测试类方法。

Hints:
提示：

Use __init__ method to construct some parameters
使用__init__方法构造一些参数

"""

class stringa:
    def __init__(self):
        self.str1= ""

    def getstring(self):
            self.str1=input("请输入字符串：")
    
    def printstring(self):
            print(self.str1.upper())

s=stringa()
s.getstring()
s.printstring()