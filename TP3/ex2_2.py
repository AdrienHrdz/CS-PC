import sys,os

(dfr1,dfw1) = os.pipe()
(dfr2,dfw2) = os.pipe()

pid1 = os.fork()

if os.getpid() == 0:
    pid2 = os.fork()

if pid2 == 0:
    #on est dans le processus petit fils
    os.close(dfr1)
    os.dup2(dfw1,1)
    os.close(dfw1)
    os.execlp('tail', 'tail', '-n', '5')

