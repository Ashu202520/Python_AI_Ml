def main():
    name = input("Enter name: ")
    letter_count = 0
    for char in name:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            letter_count += 1
    print(f"Number of letters: {letter_count}")

if __name__ == "__main__":
    main()