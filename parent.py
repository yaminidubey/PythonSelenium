class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b


    def getdata(self):
        return self.firstnumber + self.secondnumber + Calculator.num

if __name__== "__main__":
    obj = Calculator(2,3)
    print(obj.getdata())