def main():
    No1 = int(input("Enter first number: "))
    product = 1
    for i in range(1, No1 + 1):
        product = product * i
    print("The product is:", product)

if __name__ == "__main__":
    main()