def main():
    No1 = int(input("Enter a number: "))
    original = No1
    reverse = 0
    while No1 > 0:
        digit = No1 % 10
        reverse = reverse * 10 + digit
        No1 = No1 // 10
    
    print(f"Original number: {original}")
    print(f"Reversed number: {reverse}")
    
    if original == reverse:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")

if __name__ == "__main__":
    main()