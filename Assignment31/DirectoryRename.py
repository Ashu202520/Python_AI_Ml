import sys
import os


def DirectoryRename(DirName="Demo", Ext1=".txt", Ext2=".doc"):

    try:
        Border = "-"*50
        fobj = open("Marvellous.log", "w")

        fobj.write(Border+"\n")
        fobj.write("This is a log file created by Marvellous Automation\n")
        fobj.write("Directory Rename Script\n")
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

            for fname in FileName:

                if fname.endswith(Ext1):

                    OldPath = os.path.join(FolderName, fname)
                    NewName = fname.replace(Ext1, Ext2)
                    NewPath = os.path.join(FolderName, NewName)

                    os.rename(OldPath, NewPath)

                    FileCount = FileCount + 1
                    fobj.write("Renamed : "+OldPath+" -> "+NewPath+"\n")

        fobj.write(Border+"\n")
        fobj.write("Total Files Renamed : "+str(FileCount)+"\n")
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

    if(len(sys.argv) != 4):
        print("Invalid Number of Arguments")
        print("Usage : DirectoryRename.py DirectoryName OldExtension NewExtension")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

    print("Check Marvellous.log for output")


if __name__ == "__main__":
    main()