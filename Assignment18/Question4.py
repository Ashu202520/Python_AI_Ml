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

    print("Actual Data is :", numbers)

    search = int(input("Enter the element to search: "))
    count = numbers.count(search)
    print(f"Output: {count}")


if __name__ == "__main__":
    main()