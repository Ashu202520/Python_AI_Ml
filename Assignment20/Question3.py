import threading

def EvenList(Data):
    Sum = 0
    print("Even elements:")
    for i in Data:
        if i % 2 == 0:
            print(i)
            Sum = Sum + i
    print("Sum of even elements:", Sum)


def OddList(Data):
    Sum = 0
    print("Odd elements:")
    for i in Data:
        if i % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of odd elements:", Sum)


def main():
    Size = 0
    Value = 0
    Data = list()

    print("Enter the number of elements")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
