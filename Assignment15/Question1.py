def main():
    Size = 0
    Value = 0
    print("Enter the number of elements")
    Size = int(input())

    numbers = list()

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        numbers.append(Value)

    squares = list(map((lambda x: x * x), numbers))
    print("Squares list:", squares)

if __name__ == "__main__":
    main()