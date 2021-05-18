import signal, sys, os,time

def fArret(s,frame):
    print("\nsignal d'arret reçu")
    sys.exit(0)


signal.signal(signal.SIGINT,fArret)


arret = True 
while arret == True:
    print("je boucle")    
    time.sleep(2)