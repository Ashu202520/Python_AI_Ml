No1 = int(input("Enter a number: "))
Divisiable_By_Five = lambda No1: True if No1 % 5 == 0 else False
result = Divisiable_By_Five(No1)
print(f"The number {No1} is divisible by 5: {result}")