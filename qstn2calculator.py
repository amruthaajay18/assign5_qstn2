class Calculator:

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def add(self):
        sum=self.no1+self.no2
        print(sum)
    def subtract(self):
        differ=self.no2-self.no1
        print (differ)
    def multiply(self):
        mul=self.no1*self.no2
        print (mul)
    def divide(self):
        div=self.no2/self.no1
        print (div)
obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()