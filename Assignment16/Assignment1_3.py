def Add(No1, No2):
    return No1 + No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    Sum = 0
    Sum = Add(Value1, Value2)

    print("Addition is:", Sum)




if __name__ == "__main__":
    main()