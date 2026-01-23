
def main():
    Size = 0
    Value = ""
    print("Enter the string")
    Size = int(input())

    Data = list()

    print("Enter the strings :")

    for i in range(Size):
        Value = input()
        Data.append(Value)

    print("Original Data :", Data)
    RData = list(filter(lambda x: len(x) > 5, Data))
    print("Strings with length > 5 :", RData)


if __name__ == "__main__":
    main()