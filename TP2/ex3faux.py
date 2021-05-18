import sys
import os 

command = ['who','ps','ls']

for i in range(len(command)):
    #os.fork()
    print(i)
    pid = os.fork()
    os.execv('/usr/bin/'+command[i],['a'])