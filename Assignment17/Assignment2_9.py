def main():
    No1 = int(input("Enter a number: "))
    Count = 0
    while No1 > 0:
        digit = No1 % 10
        Count += 1
        No1 = No1 // 10
    print("The total digits are:", Count)

if __name__ == "__main__":
    main()