import os
import sys

def main():

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    if os.path.exists("Demo.txt") == False:
        print("Demo.txt does not exist")
        return

    fobj = open("Demo.txt", "r")
    Data = fobj.read()
    fobj.close()

    fobj2 = open(sys.argv[1], "w")
    fobj2.write(Data)
    fobj2.close()

    print("Copy contents of Demo.txt into", sys.argv[1])


if __name__ == "__main__":
    main()
