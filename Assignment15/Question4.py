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

    RData = reduce(lambda x, y: x + y, Data)
    print("Data after Addition is :", RData)

if __name__ == "__main__":
    main()