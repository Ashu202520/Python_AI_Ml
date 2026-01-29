class Numbers:

    def __init__(self, Value):
        self.Num = Value

    
    def ChkPrime(self):
        if self.Num < 2:
            return False
        for i in range(2, self.Num):
            if self.Num % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Num):
            if self.Num % i == 0:
                Sum += i
        if Sum == self.Num:
            return True
        else:
            return False
        
    def Factors(self):
        factorList = []
        for i in range(1, self.Num + 1):
            if self.Num % i == 0:
                factorList.append(i)
        return factorList
    
    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Num):
            if self.Num % i == 0:
                Sum += i
        return Sum
    


num = int(input("Enter number: "))
obj = Numbers(num)

print("Is Prime:", obj.ChkPrime())
print("Is Perfect:", obj.ChkPerfect())
print("Factors:", obj.Factors())
print("Sum of Factors:", obj.SumFactors())

print()

num2 = int(input("Enter number: "))
obj1 = Numbers(num2)

print("Is Prime:", obj1.ChkPrime())
print("Is Perfect:", obj1.ChkPerfect())
print("Factors:", obj1.Factors())
print("Sum of Factors:", obj1.SumFactors())
