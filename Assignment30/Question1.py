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
    Data = fobj.readline()
    fobj.close()

    linecount = len(Data)

    print("Number of lines in file is:", linecount)


if __name__ == "__main__":
    main()