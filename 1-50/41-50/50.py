"""
Define a class named American which has a static method called printNationality.
定义一个名为American的类,该类有一个称为printNationality的静态方法。
"""
#本人答案
class American:
    @staticmethod
    def printNationality():
        print("American")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()