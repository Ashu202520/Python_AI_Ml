import threading

def EvenFactor(No):
    sum_even = 0
    print("Even factors of", No, ":", end=" ")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum_even += i
    print()
    print("Sum of even factors:", sum_even)

def OddFactor(No):
    sum_odd = 0
    print("Odd factors of", No, ":", end=" ")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum_odd += i
    print()
    print("Sum of odd factors:", sum_odd)



def main():
    No = int(input("Enter a number: "))
    
    t1 = threading.Thread(target=EvenFactor, args=(No,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(No,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Exit from main")

if __name__ == "__main__":
    main()