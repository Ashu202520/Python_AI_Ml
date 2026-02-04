import os
import sys

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    Source = sys.argv[1]
    Destination = sys.argv[2]

    if os.path.exists(Source) == False:
        print("Source file does not exist")
        return

    fsrc = open(Source, "r")
    Data = fsrc.read()
    fsrc.close()

    fdest = open(Destination, "w")
    fdest.write(Data)
    fdest.close()

    print("Contents of", Source, "copied into", Destination)


if __name__ == "__main__":
    main()
