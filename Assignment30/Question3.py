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

    for line in fobj:
        print(line, end="")

    fobj.close()


if __name__ == "__main__":
    main()
