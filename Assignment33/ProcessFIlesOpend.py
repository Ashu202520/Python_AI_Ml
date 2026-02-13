import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Border = "-" * 50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    # CPU
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border+"\n")

    # PROCESS + OPEN FILE REPORT
    fobj.write("\nProcess Report With Open Files Count\n")
    fobj.write(Border+"\n")

    for proc in psutil.process_iter(['pid','name']):
        try:
            p = psutil.Process(proc.pid)
            open_files = p.open_files()
            count = len(open_files)

            fobj.write("Process Name : %s\n" % proc.name())
            fobj.write("PID : %s\n" % proc.pid)
            fobj.write("Number of files opened : %s\n" % count)
            fobj.write(Border+"\n")

        except psutil.AccessDenied:
            fobj.write("Process Name : %s\n" % proc.info['name'])
            fobj.write("PID : %s\n" % proc.pid)
            fobj.write("Number of files opened : Access Denied\n")
            fobj.write(Border+"\n")

        except psutil.NoSuchProcess:
            pass

    # DISK
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    # NETWORK
    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024*1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")

    fobj.write("------------End of Log File------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    Border = "-" * 50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h","--H"):
            print("Usage : Script.py TimeInterval DirectoryName")

        elif sys.argv[1] in ("--u","--U"):
            print("TimeInterval : minutes")
            print("DirectoryName : folder for logs")

        else:
            print("Invalid argument")

    elif len(sys.argv) == 3:

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Automation started...")
        print("Press Ctrl+C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid parameters")

if __name__ == "__main__":
    main()
