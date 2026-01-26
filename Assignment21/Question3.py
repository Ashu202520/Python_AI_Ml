import threading

Counter = 0
LockObj = threading.Lock()

def Increment():
    global Counter
    for i in range(1000):
        LockObj.acquire()
        Counter = Counter + 1
        LockObj.release()


def main():
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final value of counter:", Counter)


if __name__ == "__main__":
    main()
