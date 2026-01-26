def main():
    No1 = int(input("Enter a number: "))
    for i in range(No1):
        for j in range(1, No1 + 1):
            print(j, end=" ")
        print()


if __name__ == "__main__":
    main()