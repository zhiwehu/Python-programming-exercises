"""
Define a custom exception class which takes a string message as attribute.
定义一个自定义异常类，该类将字符串消息作为属性。

Hints:
提示：

To define a custom exception, we need to define a class inherited from Exception.
要定义自定义异常，我们需要定义一个从exception继承的类。
"""

#本人答案
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)