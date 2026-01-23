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

    RData = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, Data))
    print("The number is both divisible by 3 and 5 :", RData)

if __name__ == "__main__":
    main()