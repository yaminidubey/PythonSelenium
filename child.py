from parent import Calculator


class Child (Calculator):
    num1 = 200


    def  __init__(self):
        Calculator.__init__(self, 9, 10)


    def getcomplete_data(self):
        return self.num + self.num1 + self.getdata()

obj = Child()
print(obj.getcomplete_data())



