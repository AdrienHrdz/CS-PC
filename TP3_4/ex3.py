import signal, sys, os,time

def fArret(s,frame):
    print("\nsignal d'arret reçu")
    global fin #recup la var globale
    fin = True

#ignore le ctrl+C
#signal.signal(signal.SIGINT,signal.SIG_IGN)


signal.signal(signal.SIGINT,fArret)
#commande pour tuer
# kill -KILL PID
fin = False 
while fin == False:
    print("je boucle")    
    time.sleep(2)