def Area1(No1,No2):
    Area = No1 * No2
    return Area


def main():

    Length = float(input("Enter first number: "))
    Width = float(input("Enter second number: "))

    Areaofrectangle = Area1(Length, Width)
    print(f"Area of rectangle is: {Areaofrectangle}")


if __name__ == "__main__":
    main()