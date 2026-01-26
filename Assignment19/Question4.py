from functools import reduce

def Incerment(No):
    if No % 2 == 0:
        return True
    return False

def Square(No):
    return No * No


def Addition(x, y):
    return x + y

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

    FData = list(filter(Incerment, Data))
    print("Data after filter is :", FData)

    MData = list(map(Square, FData))
    print("Data after map is :", MData)

    RData = reduce(Addition, MData)
    print("Result after reduce is :", RData)


if __name__ == "__main__":
    main()