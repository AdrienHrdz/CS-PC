import sys, os, random

#génération de la liste aléatoire
n = random.randint(0,50)
L = []
for k in range(n):
    L.append(random.randint(0,50))
Somme = 0


#processus P1
P1 = os.fork()
if P1 == 0:
    i = 1
    SommeImpairs = 0
    while i < n:
        SommeImpairs = SommeImpairs + L[i]
        i = i + 2
        print("Somme impaire : ",SommeImpairs)
    Somme = Somme + SommeImpairs

#processus P2
P2 = os.fork()
if P2 == 0 :
    i = 0
    SommePairs = 0
    while i < n:
        SommePairs = SommePairs + L[i]
        i = i + 2
        print("Somme pairs : ", SommePairs)
    Somme = Somme + SommePairs


if os.getpid() != 0:
    print("valeur de la somme : ", Somme)