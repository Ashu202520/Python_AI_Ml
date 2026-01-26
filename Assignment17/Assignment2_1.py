def Add(No1, No2):
    return No1 + No2

def Sub(No1, No2):
    return No1 - No2

def Mult(No1, No2):
    return No1 * No2

def Div(No1, No2):
    return No1 / No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    print("Addition:", Add(Value1, Value2))
    print("Subtraction:", Sub(Value1, Value2))
    print("Multiplication:", Mult(Value1, Value2))
    print("Division:", Div(Value1, Value2))

if __name__ == "__main__":
    main()