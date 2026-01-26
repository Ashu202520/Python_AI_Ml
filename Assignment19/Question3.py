from functools import reduce

def Incerment(No):
    return No + 10

def FilterOut(No):
    if No >= 70 and No <= 90:
        return True
    return False

def Multiply(x, y):
    return x * y

def main():
    Size = 0
    Value = 0
    print("Enter the number of elements")
    Size = int(input())


    Data = list()
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    print(Data)

    print("Enter the elements :")

    FData = list(filter(FilterOut, Data))
    print("Data after filter is :", FData)

    MData = list(map(Incerment, FData))
    print("Data after map is :", MData)

    RData = reduce(Multiply, MData)
    print("Result after reduce is :", RData)


if __name__ == "__main__":
    main()