import os

def main():
    FileName = input("Enter the file name: ")
    Ret = os.path.exists(FileName)
    if(Ret == True):
        print("File is exist")
    else:
        print("File is not exist")

    fobj = open(FileName, "r")
    Data = fobj.read()
    
    print(Data)

    fobj.close()



if __name__ == "__main__":
    main()