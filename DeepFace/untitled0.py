import os

root = "/mnt/NVME1/Work/"

filelist = os.listdir(root)

datelist = []
for i in filelist:
    file = root + i
    info = os.stat(file)
    temp = (info[8], file)
    datelist.append(temp)
    print(temp)

datelist.sort()

y = 0

for x in datelist:
    file = x[1]
    ext = file.split(".")[1]
    os.rename(file, f"{root}{y}.{ext}")
    y += 1
