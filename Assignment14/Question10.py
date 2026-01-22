No1 = int(input("Enter a number: "))
No2 = int(input("Enter another number: "))
No3 = int(input("Enter a third number: "))
Largest_Among_Three = lambda No1, No2, No3: No1 if No1 > No2 and No1 > No3 else No2 if No2 > No1 and No2 > No3 else No3
result = Largest_Among_Three(No1, No2, No3)
print(f"The largest among {No1}, {No2}, and {No3} is: {result}")