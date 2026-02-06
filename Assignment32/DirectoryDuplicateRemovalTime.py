import sys
import os
import hashlib
import time


def Checksum(path):

    hobj = hashlib.md5()
    fobj = open(path,'rb')

    buffer = fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DuplicateRemoval(DirName="Demo"):

    fd = open("Log.txt","w")
    Result = {}

    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for fname in FileName:

            path = os.path.join(FolderName,fname)
            hash = Checksum(path)

            if hash in Result:
                fd.write(path+"\n")
                os.remove(path)
            else:
                Result[hash] = path

    fd.close()


def main():

    start = time.time()

    if(len(sys.argv)!=2):
        print("Usage : DirectoryDuplicateRemovalTime.py Demo")
        return

    DuplicateRemoval(sys.argv[1])

    end = time.time()

    print("Execution time :", end-start)


if __name__=="__main__":
    main()
