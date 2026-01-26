def main():
    No1 = int(input("Enter a number: "))
    Sum = 0
    for i in range(1, No1):
        if No1 % i == 0:
            Sum += i
    print(f"Addition of factors of {No1} is: {Sum}")

if __name__ == "__main__":
    main()