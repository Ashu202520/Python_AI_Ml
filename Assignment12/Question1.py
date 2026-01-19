def main():
    Char = input("Enter a character: ")
    if Char == "a" or Char == "e" or Char == "i" or Char == "o" or Char == "u" or \
       Char == "A" or Char == "E" or Char == "I" or Char == "O" or Char == "U":
        print(f"{Char} is a vowel.")
    else:
        print(f"{Char} is not a vowel.")


if __name__ == "__main__":
    main()