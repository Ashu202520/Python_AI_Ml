def DivisiablebleBy5(Num):
    if(Num % 5 == 0):
        return True
    else:
        return False

def main():
    Num = int(input("Enter a number: "))
    if DivisiablebleBy5(Num):
        print(f"{Num} is divisible by 5")
    else:
        print(f"{Num} is not divisible by 5")



if __name__ == "__main__":
    main()