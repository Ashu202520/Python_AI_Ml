def Minnumber(numbers, size):
    if numbers == []:
        return 0
    min = numbers[0]
    for i in range(size):
        if numbers[i] < min:
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
    
    Mini = Minnumber(numbers, size)
    print("Minimum number from list is :", Mini)


if __name__ == "__main__":
    main()