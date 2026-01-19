def ChkGreater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    greater = ChkGreater(number1, number2)
    print(f"The greater number is: {greater}")

if __name__ == "__main__":
    main()
