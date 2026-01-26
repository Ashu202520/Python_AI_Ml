def main():
    No1 = int(input("Enter a number: "))
    for i in range(No1, 0, -1):
        print(*"*" * (i))

if __name__ == "__main__":
    main()