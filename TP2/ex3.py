import os
import sys

pid = os.fork()

if pid == 0:
    os.execlp('who','a')  #command , arg par défaut, autres arg
#os.wait()

pid1 = os.fork()
if pid1 == 0:
    os.execlp('ps','a')
#os.wait()

pid2 = os.fork()
if pid2 == 0:
    os.execlp('ls','a', '-l')
