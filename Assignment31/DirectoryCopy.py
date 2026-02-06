import sys
import os


def CopyFile(Source, Destination):

    fsrc = open(Source, "rb")
    data = fsrc.read()
    fsrc.close()

    fdest = open(Destination, "wb")
    fdest.write(data)
    fdest.close()


def DirectoryCopy(Src="Demo", Dest="Demo"):

    try:
        Border = "-"*50
        fobj = open("Marvellous.log", "w")

        fobj.write(Border+"\n")
        fobj.write("This is a log file created by Marvellous Automation\n")
        fobj.write("Directory Copy Script (Without shutil)\n")
        fobj.write(Border+"\n")

        if not os.path.exists(Src):
            fobj.write("Source directory does not exist\n")
            return

        if not os.path.isdir(Src):
            fobj.write("Source is not a directory\n")
            return

        if not os.path.exists(Dest):
            os.mkdir(Dest)
            fobj.write("Destination directory created\n")

        FileCount = 0

        for FolderName, SubFolderName, FileName in os.walk(Src):

            for fname in FileName:

                SrcPath = os.path.join(FolderName, fname)
                DestPath = os.path.join(Dest, fname)

                CopyFile(SrcPath, DestPath)

                FileCount = FileCount + 1
                fobj.write("Copied : "+SrcPath+" -> "+DestPath+"\n")

        fobj.write(Border+"\n")
        fobj.write("Total Files Copied : "+str(FileCount)+"\n")
        fobj.write(Border+"\n")

        fobj.close()

    except Exception as e:
        fobj.write("Error occured : "+str(e)+"\n")


def main():

    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Usage : DirectoryCopy.py SourceDir DestDir")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

    print("Check Marvellous.log for output")


if __name__ == "__main__":
    main()
