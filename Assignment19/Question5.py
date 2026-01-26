from functools import reduce

def Prime(No):
    if No < 2:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Square(No):
    return No * 2


def Maxnumber(x, y):
    if x > y:
        return x
    return y
    

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

    FData = list(filter(Prime, Data))
    print("Data after filter is :", FData)

    MData = list(map(Square, FData))
    print("Data after map is :", MData)

    RData = reduce(Maxnumber, MData)
    print("Result after reduce is :", RData)


if __name__ == "__main__":
    main()