import threading

def Thread1():
    print("Thread1 output:")
    for i in range(1, 51):
        print(i)
    print("Thread1 completed")
    print()

def Thread2():
    print("Thread2 output:")
    for i in range(50, 0, -1):
        print(i)
    print("Thread2 completed")
    print()


def main():
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
