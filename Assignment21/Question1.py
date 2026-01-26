import threading

def is_prime(No):
    if No < 2:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True


def Prime(Data):
    print("Prime numbers:")
    for i in Data:
        if is_prime(i):
            print(i)


def NonPrime(Data):
    print("Non-prime numbers:")
    for i in Data:
        if not is_prime(i):
            print(i)


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

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
