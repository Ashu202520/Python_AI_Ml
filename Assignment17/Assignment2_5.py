def main():
    No1 = int(input("Enter a number:"))
    if No1 <= 1:
        print("Its not a prime number: ", No1)
        return
    for i in range(2, No1):
        if No1 % i == 0:
            print("Its not a prime number: ", No1)
            return
    print("Its a prime number: ", No1)

if __name__ == "__main__":
    main()