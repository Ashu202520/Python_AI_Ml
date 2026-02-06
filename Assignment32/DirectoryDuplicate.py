import sys
import os
import hashlib


def Checksum(path):

    hobj = hashlib.md5()
    fobj = open(path,'rb')

    buffer = fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DirectoryDuplicate(DirName="Demo"):

    try:
        fd = open("Log.txt","w")
        Result = {}

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            for fname in FileName:
                path = os.path.join(FolderName,fname)
                hash = Checksum(path)

                if hash in Result:
                    fd.write(path+"\n")
                else:
                    Result[hash] = path

        fd.close()

    except Exception as e:
        print("Error :",e)


def main():

    if(len(sys.argv)!=2):
        print("Usage : DirectoryDuplicate.py Demo")
        return

    DirectoryDuplicate(sys.argv[1])


if __name__=="__main__":
    main()
