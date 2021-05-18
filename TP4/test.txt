import sys, random
import multiprocessing as mp

def SommeImp(L,sem):
    i = 1
    SommeImpairs = 0
    while i < n:
        SommeImpairs = SommeImpairs + L[i]
        i = i + 2
        print("Somme impaire : ",SommeImpairs)
    sem.acquire()
    Somme.value += SommeImpairs
    sem.release()
    sys.exit(0)

def SommePair(L,sem):
    i = 0
    SommePairs = 0
    while i < n:
        SommePairs = SommePairs + L[i]
        i = i + 2
        print("Somme pairs : ", SommePairs)
    sem.acquire()
    Somme.value += SommePairs
    sem.release()
    sys.exit(0)

#mémoire partagée
Somme = mp.Value("i",0)

#génération de la liste aléatoire
n = 25 #random.randint(1,10)
L = []
for k in range(n):
    L.append(random.randint(0,50))
print(L)

#créarion sémaphore
sem = mp.Semaphore(1)

if __name__ == '__main__':
    P1 = mp.Process(target=SommeImp, args=(L,sem))
    P2 = mp.Process(target=SommePair, args=(L,sem))
    
    P1.start()
    P2.start()

    P1.join() 
    P2.join()

    print("Somme totale = ",Somme.value)