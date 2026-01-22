def Area1(No1,No2):
    print("Inside Area1 function")
    Area = No1 * No2
    return Area


def main():

    radius = float(input("Enter radius of circle: "))
    pi = 3.14

    Areaofcircle = Area1(pi, radius * radius)
    print(f"Area of circle is: {Areaofcircle}")



if __name__ == "__main__":
    main()