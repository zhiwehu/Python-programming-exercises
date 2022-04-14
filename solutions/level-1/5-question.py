# Solution

class Yeah:
    def __init__(self):
        self.inp = input("Enter string: ")
        self.getString = self.getString

    def getString(self):
        printString = self.inp
        print(printString.upper())
        return printString.upper()

    def testGetString(self, actual):
        test = self.getString()
        if (test == actual and type(test) is type(actual)):
            print("Test Passed")
        else:
            print("Test Failed :(")


jaden = Yeah()

# jaden.getString()

jaden.testGetString("YEAH")
