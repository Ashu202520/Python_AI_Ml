def sum(numbers, size):
    Addition = 0
    for i in range(size):
        Addition += numbers[i]
    return Addition

def main():
    size = 0
    value = 0
    print("Enter the elements")

    size = int(input())

    numbers = list()

    print("Enter the elements :")
    for i in range(size):
        value = int(input())
        numbers.append(value)
    
    Addition = sum(numbers, size)
    print("Addition of elements is :", Addition)


if __name__ == "__main__":
    main()