"""
Define a class named American and its subclass NewYorker.
定义一个名为American的类及其子类NewYorker。
"""
#本人答案
class American:
    @staticmethod
    def printNationality():
        print("American")

class NewYorker(American):
    @staticmethod
    def printNationality():
        print("New Yorker")