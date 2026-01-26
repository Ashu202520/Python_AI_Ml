import threading

def SumElements(Data, Result):
    Sum = 0
    for i in Data:
        Sum = Sum + i
    Result[0] = Sum


def ProductElements(Data, Result):
    Product = 1
    for i in Data:
        Product = Product * i
    Result[1] = Product


def main():
    Size = 0
    Value = 0
    Data = list()
    Result = [0, 0]

    print("Enter the number of elements")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    t1 = threading.Thread(target=SumElements, args=(Data, Result))
    t2 = threading.Thread(target=ProductElements, args=(Data, Result))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", Result[0])
    print("Product of elements:", Result[1])


if __name__ == "__main__":
    main()
