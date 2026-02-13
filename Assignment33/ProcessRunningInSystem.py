import psutil
import sys
import os
import time
import schedule



def CreateLog(FolderName):
    Border = "-"*50
    print(Border)

    Ret = False
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to create folder")
            return 
    else:
        os.mkdir(FolderName)
        print("Directory for log files get created Successfully")
    
    timestamp= time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "MArvellous_%s.log" %timestamp)
    print("Log File gets created with name: ", FileName)

    fobj = open(FileName, "w")
    
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at :"+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------System Report------------------------\n")


    #print("CPU Usage:", psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    #print("RAM Usage : ", mem.percent)

    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    process_name = psutil.process_iter()
    fobj.write("\nProcess Report\n")
    for eachprocess in process_name:

        fobj.write("Process running in the system : %s\n" %eachprocess.name())
        fobj.write(Border+"\n")
    
    
    fobj.write("\nDisk Usage Report\n")

    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))

        except:
            print("Inside Expection")
    fobj.write(Border+"\n")
    
    
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")

    # Process Log

    fobj.write(Border+"\n")
    fobj.write("------------End of Log File-------")
    fobj.write(Border+"\n")



def main():

    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to:")
            print("1: Create automatic logs")
            print("2: Executes perodically")
            print("3: Sends mail with the log")
            print("4: Store information about the processess")
            print("5: Store information about the CPU")
            print("6: Store information about RAM")
            print("7: Store information about Secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoyName")
            print("TImeInterval : The time in  minutes for periodic scheduling")
            print("DirectoryName : Namew of directory to create auto logs")
        

        else:
            print("Invalid number of argument")
            print("Unable to process as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval :" , sys.argv[1])
        print("Directory Name :" , sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Marvellous Platform Surveillance System Started Successfully")
        print("Directory Created with Name :", sys.argv[2])
        print("Time interval in Minutes:" , sys.argv[1])
        print("Press Ctrl + C to stop the execuation")
        

        # Wait Till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
            print("Unable to process as there is no such option")
            print("Please use --h or --u to get more details")
            


    print(Border)
    print("--------Thank You for using our script------------")
    print(Border)
    


if __name__ == "__main__":
    main()