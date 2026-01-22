No1 = int(input("Enter a number: "))
No2 = int(input("Enter another number: "))
Min_Num = lambda No1, No2: No1 if No1 < No2 else No2
print(f"The smaller number between {No1} and {No2} is {Min_Num(No1, No2)}")