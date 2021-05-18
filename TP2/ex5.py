import os, sys, time
# Lecture du nombre de processus
if len(sys.argv) == 1 :
    print("Pas de processus à créer")
    sys.exit()

if sys.argv[1].isnumeric() == True:
    N = int(sys.argv[1])
else:
    print("Erreur : entrée non valide")
    sys.exit()
print(N)

#Création des N processus
pid = os.getpid()               
for i in range(N+1):
    if pid != 0:
        pid = os.fork()
    else:
        print('pid fils : ', os.getpid(),'pid pere : ', os.getppid())
        time.sleep(2*i)
        sys.exit(i)

