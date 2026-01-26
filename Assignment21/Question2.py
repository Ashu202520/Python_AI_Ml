import threading

def MaxNumber(Data):
    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i
    print("Maximum element:", Max)


def MinNumber(Data):
    Min = Data[0]
    for i in Data:
        if i < Min:
            Min = i
    print("Minimum element:", Min)


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

    t1 = threading.Thread(target=MaxNumber, args=(Data,), name="Thread1")
    t2 = threading.Thread(target=MinNumber, args=(Data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

