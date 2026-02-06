import sys
import os


def DirectoryScanner(DirName="Demo", Ext=".txt"):

    try:
        Border = "-"*50
        fobj = open("Marvellous.log", "w")

        fobj.write(Border+"\n")
        fobj.write("This is a log file created by Marvellous Automation\n")
        fobj.write("Directory File Search Script\n")
        fobj.write(Border+"\n")

        Ret = os.path.exists(DirName)

        if(Ret == False):
            fobj.write("There is no such directory\n")
            return

        Ret = os.path.isdir(DirName)

        if(Ret == False):
            fobj.write("Unable to scan as there is not any directory\n")
            return

        FileCount = 0

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            for Fname in FileName:
                if Fname.endswith(Ext):
                    FileCount = FileCount + 1
                    FullPath = os.path.join(FolderName, Fname)
                    fobj.write(FullPath+"\n")

        fobj.write(Border+"\n")
        fobj.write("Total Files Found : "+str(FileCount)+"\n")
        fobj.write(Border+"\n")

        fobj.close()

    except PermissionError:
        fobj.write("Permission denied\n")

    except Exception as e:
        fobj.write("Error occured : "+str(e)+"\n")


def main():

    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Usage : DirectoryFileSearch.py DirectoryName Extension")
        return

    DirectoryScanner(sys.argv[1], sys.argv[2])

    print("Check Marvellous.log for output")


if __name__ == "__main__":
    main()