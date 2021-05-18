import signal, sys, os,time

def fArret(s,frame):
    print("\nsignal d'arret reçu")
    sys.exit(0)

#ignore le ctrl+C
signal.signal(signal.SIGINT,signal.SIG_IGN)

#commande pour tuer
# kill -KILL PID
arret = True 
while arret == True:
    print("je boucle")    
    time.sleep(2)