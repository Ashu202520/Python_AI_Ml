def main():
    No1 = int(input("Enter a number: "))
    for i in range(No1):
        print(*"*" * (No1))

if __name__ == "__main__":
    main()