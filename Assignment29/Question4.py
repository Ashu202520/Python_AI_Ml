import os
import sys

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    if os.path.exists(File1) == False or os.path.exists(File2) == False:
        print("One or both files do not exist")
        return

    fobj = open(File1, "r")
    Data1 = fobj.read()
    fobj.close()

    fobj2 = open(File2, "r")
    Data2 = fobj2.read()
    fobj2.close()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()
