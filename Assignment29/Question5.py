import os
import sys

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    Fname = sys.argv[1]
    Sname = sys.argv[2]

    if os.path.exists(Fname) == False:
        print("File does not exist")
        return

    fobj = open(Fname, "r")
    Data = fobj.read()
    fobj.close()

    words = Data.split()
    occurrence = words.count(Sname)

    print("Frequency of", Sname, "is:", occurrence)

if __name__ == "__main__":
    main()
