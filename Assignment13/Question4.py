def main():
    No1 = int(input("Enter a number:"))
    binary_without_prefix = format(No1, 'b') 
    print(f"The binary representation of {No1} is: {binary_without_prefix}")



if __name__ == "__main__":
    main()