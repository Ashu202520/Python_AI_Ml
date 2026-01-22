No1 = int(input("Enter a number: "))
Odd_Num = lambda No1: True if No1 % 2 != 0 else False
result = Odd_Num(No1)
print(f"The number {No1} is odd: {result}")