import psutil
import sys
import os
import time
import schedule
import Mail

def CreateLog(FolderName, Receiver):

    Border = "-"*50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    # CPU & RAM
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border+"\n")

    MemoryList = []

    fobj.write("\nProcess Report With PID and Open Files\n")
    fobj.write(Border+"\n")

    for eachprocess in psutil.process_iter():
        try:
            proc = psutil.Process(eachprocess.pid)

            open_file = proc.open_files()
            num_open_file = len(open_file)

            meminfo = proc.memory_info()
            rss = meminfo.rss/(1024*1024)
            vms = meminfo.vms/(1024*1024)
            mem_percent = proc.memory_percent()

            MemoryList.append((eachprocess.name(),eachprocess.pid,rss,vms,mem_percent))

            fobj.write("Process : %s\n" % eachprocess.name())
            fobj.write("PID : %s\n" % eachprocess.pid)
            fobj.write("Open Files : %s\n" % num_open_file)
            fobj.write(Border+"\n")

        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass

    # Top 10 memory processes
    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border+"\n")

    MemoryList.sort(key=lambda x:x[2], reverse=True)

    for data in MemoryList[:10]:
        fobj.write("Process : %s\n"%data[0])
        fobj.write("PID : %s\n"%data[1])
        fobj.write("RSS : %.2f MB\n"%data[2])
        fobj.write("VMS : %.2f MB\n"%data[3])
        fobj.write("Memory %% : %.2f\n"%data[4])
        fobj.write(Border+"\n")

    # Disk usage
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n"%(part.mountpoint, usage.percent))
        except:
            pass

    # Network
    net = psutil.net_io_counters()
    fobj.write(Border+"\n")
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n"%(net.bytes_sent/(1024*1024)))
    fobj.write("Recv : %.2f MB\n"%(net.bytes_recv/(1024*1024)))
    fobj.write(Border+"\n")

    fobj.write("------------End of Log File-------\n")
    fobj.write(Border+"\n")

    fobj.close()

    # MAIL SECTION
    subject = "Marvellous System Report"
    body = "Total Processes : %s\nLog attached." % len(list(psutil.process_iter()))

    Mail.send_mail(
        "ashutoshdhavalshankh@gmail.com",
        "rlqn qmnl cale jjmc",
        Receiver,
        subject,
        body,
        FileName
    )

def main():

    if(len(sys.argv)==4):

        Folder=sys.argv[1]
        Receiver=sys.argv[2]
        Interval=int(sys.argv[3])

        schedule.every(Interval).minutes.do(CreateLog,Folder,Receiver)

        print("System Started")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("python PlatformSurveillance.py Logs receiver@gmail.com 10")

if __name__=="__main__":
    main()
