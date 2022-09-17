import time, psutil, os

while True:
    sysyear = time.ctime()
    systime = sysyear[11:19]
    print(systime)
    print(systime[0:2])
    if "java" not in (i.name() for i in psutil.process_iter()):
        if int(systime[0:2]) > 12 or int(systime[0:2]) < 6:
            print("Java is not running! Time for a shutdown!")
            time.sleep(5)
            os.system("shutdown /s /t 1")
        else:
             print("Java crashed? Time for a restart!")
             time.sleep(5)
             os.system("shutdown /r /t 1")
    else: print("Everything seems fine")
    time.sleep(60)