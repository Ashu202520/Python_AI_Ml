No1 = int(input("Enter a number: "))
No2 = int(input("Enter another number: "))
Large_Num = lambda No1, No2: No1 if No1 > No2 else No2
print(f"The larger number between {No1} and {No2} is {Large_Num(No1, No2)}")