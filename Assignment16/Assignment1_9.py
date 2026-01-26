def main():
    print("First 10 even numbers:")
    count = 0
    num = 1
    while count < 10:
        if num % 2 == 0:
            print(num)
            count += 1
        num += 1


if __name__ == "__main__":
    main()