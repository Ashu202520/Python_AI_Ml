def main():
    No1 = int(input("Enter first number: "))
    for i in range(1, No1 + 1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    main()