def Max(numbers, size):
    if numbers == []:
        return 0
    max = numbers[0]
    for i in range(size):
        if numbers[i] > max:
            max = numbers[i]
    return max

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
    
    Maximum = Max(numbers, size)
    print("Maximum number from list is :", Maximum)


if __name__ == "__main__":
    main()