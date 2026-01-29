class Arithmetic:
    def __init__(self, Value1 = 0, Value2 = 0):
        self.Value1 = Value1
        self.Value2 = Value2
    
    def Accept(self):
        self.Value1 = int(input("Enter first number:"))
        self.Value2 = int(input("Enter second number:"))
    
    def Addition(self):
        Ans = 0
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Subtraction(self):
        Ans = 0
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.Value1 / self.Value2
        return Ans
    
obj1 = Arithmetic()
obj1.Accept()

Ret= obj1.Addition()
print("Addition is :", Ret)

Ret= obj1.Subtraction()
print("Subtraction is :", Ret)

Ret= obj1.Multiplication()
print("Multiplication is :", Ret)
Ret= obj1.Division()
print("Division is :", Ret)


        