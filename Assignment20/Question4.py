import threading

def Small(Data):
    Count = 0
    for ch in Data:
        if ch >= 'a' and ch <= 'z':
            Count = Count + 1

    print("Small thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters:", Count)
    print()


def Capital(Data):
    Count = 0
    for ch in Data:
        if ch >= 'A' and ch <= 'Z':
            Count = Count + 1

    print("Capital thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of uppercase characters:", Count)
    print()


def Digits(Data):
    Count = 0
    for ch in Data:
        if ch >= '0' and ch <= '9':
            Count = Count + 1

    print("Digits thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of digits:", Count)
    print()


def main():
    print("Enter the string")
    Data = input()

    t1 = threading.Thread(target=Small, args=(Data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Data,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Data,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
