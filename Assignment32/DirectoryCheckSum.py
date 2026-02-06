import sys
import os
import hashlib


def Checksum(path):

    hobj = hashlib.md5()

    fobj = open(path,'rb')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def DirectoryChecksum(DirName="Demo"):

    try:
        if not os.path.exists(DirName):
            print("Directory not found")
            return

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            for fname in FileName:
                path = os.path.join(FolderName,fname)
                print(fname," : ",Checksum(path))

    except Exception as e:
        print("Error :",e)


def main():

    if(len(sys.argv)!=2):
        print("Usage : DirectoryChecksum.py Demo")
        return

    DirectoryChecksum(sys.argv[1])


if __name__=="__main__":
    main()
