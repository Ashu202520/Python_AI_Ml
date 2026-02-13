import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Border = "-"*50
    print(Border)

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

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    print("Log File gets created with name: ", FileName)

    fobj = open(FileName, "w")
    
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at :"+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------System Report------------------------\n")

    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    process_name = psutil.process_iter()

    MemoryList = []

    fobj.write("\nProcess Report With PID and Open Files\n")

    for eachprocess in process_name:
        try:
            proc = psutil.Process(eachprocess.pid)

            open_file = proc.open_files()
            num_open_file = len(open_file)

            meminfo = proc.memory_info()

            rss = meminfo.rss / (1024*1024)
            vms = meminfo.vms / (1024*1024)
            mem_percent = proc.memory_percent()

            MemoryList.append((eachprocess.name(), eachprocess.pid, rss, vms, mem_percent))

            fobj.write("Process running in the system : %s\n" %eachprocess.name())
            fobj.write("PID : %s\n" %eachprocess.pid)
            fobj.write("Number of files open : %s\n" %num_open_file)
            fobj.write(Border+"\n")

        except psutil.AccessDenied:
            fobj.write("Process running in the system : %s\n" %eachprocess.name())
            fobj.write("PID : %s\n" %eachprocess.pid)
            fobj.write("Access Denied\n")
            fobj.write(Border+"\n")

        except psutil.NoSuchProcess:
            pass

    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border+"\n")

    MemoryList.sort(key=lambda x: x[2], reverse=True)

    for data in MemoryList[:10]:
        fobj.write("Process : %s\n" %data[0])
        fobj.write("PID : %s\n" %data[1])
        fobj.write("RSS : %.2f MB\n" %data[2])
        fobj.write("VMS : %.2f MB\n" %data[3])
        fobj.write("Memory Percentage : %.2f\n" %data[4])
        fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")
    
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")

    fobj.write("------------End of Log File-------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Use : Script.py TimeInterval DirectoryName")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("ScriptName.py TimeInterval DirectoyName")

        else:
            print("Invalid number of argument")

    elif(len(sys.argv) == 3):

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("System Started")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid parameters")

if __name__ == "__main__":
    main()
