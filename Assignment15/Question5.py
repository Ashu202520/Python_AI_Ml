from functools import reduce

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

    RData = reduce(lambda x, y: x if x > y else y, Data)
    print("Maximum number is :", RData)

if __name__ == "__main__":
    main()