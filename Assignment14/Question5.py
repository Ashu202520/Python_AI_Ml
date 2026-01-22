No1 = int(input("Enter a number: "))
Even_Num = lambda No1: True if No1 % 2 == 0 else False
result = Even_Num(No1)
print(f"The number {No1} is even: {result}")