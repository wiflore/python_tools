import datetime
print(datetime.datetime.now())
print(datetime.datetime.now())
now = datetime.datetime.now()
datevar = datetime.datetime(2017, 4, 2, 21, 23, 22, 323132)
delta = (now - datevar)
print(delta)
print(delta.total_seconds())
print(now.strftime("%Y/%m/%d/%H/%M/%S/%f"))
print(now.strftime("%B %y %m"))

filename = now

#create an empty file

def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt", "w") as file:
        file.write("")

create_file()

lst = []
import time
for i in range(2):
    lst.append(datetime.datetime.now())
    time.sleep(1)

print(lst)

for i in lst:
    print(i)