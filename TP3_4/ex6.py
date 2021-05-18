import signal, sys, os,time

def fArret(s,frame):
    print("\nsignal d'arret reçu")
    sys.exit(1)

def fInterception(s,frame):
    print("interception du ^C")
    signal.signal(signal.SIGINT,fInterception)


#création du processus fils
pid = os.fork()


if pid == 0:
    
    signal.signal(signal.SIGINT,fInterception)
    while True:
        time.sleep(1)
        print("je suis le fils")

if pid != 0:
    for k in range(6):
        time.sleep(2)
        print("je suis le père à l'itération ",k)