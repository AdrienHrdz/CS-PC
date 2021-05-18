import sys, os
#test
#test2
msg = "Antoine c'est le meilleur"
msg = msg.encode('ascii')
print("Création d'un nouveau pipe")
(dfr,dfw) = os.pipe()
n = os.write(dfw, msg)
print("le processus %d a transmis le message %s\n"%(os.getpid(), msg.decode()))
msgRecu = os.read(dfr, len(msg))
print("le processus %d a recu le message %s\n" %(os.getpid(),msgRecu.decode()))
os.close(dfr)
os.close(dfw)
sys.exit(0)