def main():
    No1 = int(input("Enter a number: "))
    Count = 0
    while No1 > 0:
        digit = No1 % 10
        Count += digit
        No1 = No1 // 10
    print("The sum of digits are:", Count)

if __name__ == "__main__":
    main()