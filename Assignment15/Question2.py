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

    print("Actual Data is :", Data)

    FData = list(filter((lambda x: (x % 2 == 0)), Data))
    print("Data after filter is :", FData)


if __name__ == "__main__":
    main()