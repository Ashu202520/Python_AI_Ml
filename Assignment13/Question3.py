def main():
    No1 = int(input("Enter a number: "))
    sum_divisors = 0
    for i in range(1, No1):
        if No1 % i == 0:
            sum_divisors += i
    
    if sum_divisors == No1:
        print(f"{No1} is a perfect number")
    else:
        print(f"{No1} is not a perfect number")

if __name__ == "__main__":
    main()