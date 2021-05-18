(dfr,dfw) = os.pipe()
import sys, os
msg = "Antoine c'est le meilleur"
msg = msg.encode('ascii')
msgRecu = os.read(dfr, len(msg))
n = os.write(dfw, msg)
os.close(dfr)
os.close(dfw)
print("Création d'un nouveau pipe")
print("le processus %d a recu le message %s\n" %(os.getpid(),msgRecu.decode()))
print("le processus %d a transmis le message %s\n"%(os.getpid(), msg.decode()))
sys.exit(0)
#test
#test2
