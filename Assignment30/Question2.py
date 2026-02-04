import os
import sys

def main():

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    Fname = sys.argv[1]

    if os.path.exists(Fname) == False:
        print("File does not exist")
        return

    fobj = open(Fname, "r")
    Data = fobj.read()
    fobj.close()

    words = Data.split()
    wordcount = len(words)

    print("Number of words in file is:", wordcount)


if __name__ == "__main__":
    main()