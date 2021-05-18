import os
import sys

ppid = os.getpid()
print("ppid : ",ppid)
for i in range(3):
    if (os.fork()!=0 ):
        os.wait()
    else:
        ppid = os.fork()
        pid = os.getpid()
        print("(i : ",i, ") ","je suis le processus : ",pid, "mon père est : ",ppid)