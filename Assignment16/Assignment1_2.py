def CheckEven(No1):
    if(No1 % 2 == 0):
        return True
    else:
        return False


def main():
    print("Enter number:")
    Value = int(input())

    Number = CheckEven(Value)

    if(Number == True):
        print(f"{Value} is Even")
    else:
        print(f"{Value} is Odd")

if __name__ == "__main__":
    main()