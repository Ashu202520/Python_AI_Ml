def main():
    Size = 0
    Value = 0
    print("Enter the number of elements")
    Size = int(input())

    Data = list()

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Original Data :", Data)
    
    EvenCount = len(list(filter(lambda x: x % 2 == 0, Data)))
    print("Count of even numbers :", EvenCount)

if __name__ == "__main__":
    main()