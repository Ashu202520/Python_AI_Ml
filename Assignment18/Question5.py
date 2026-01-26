from MarvelousNum import IsPrime

def ListPrime(numbers):
    total = 0
    for num in numbers:
        if IsPrime(num):
            total += num
    return total

def main():
    size = 0
    value = 0
    print("Enter the number of elements")

    size = int(input())

    numbers = list()

    print("Enter the elements :")
    for i in range(size):
        value = int(input())
        numbers.append(value)

    print("Input Elements :", numbers)

    result = ListPrime(numbers)
    print(f"Output: {result}")


if __name__ == "__main__":
    main()