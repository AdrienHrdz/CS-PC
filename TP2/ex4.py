import os
import sys

n = 0
for i in range(1,5):
    fils_pid = os.fork()
    if fils_pid > 0:
        os.wait()
        n = i*2
        break
print("n = ", n)
sys.exit(0)

#crea d'un processus fils par le père et attente dans le wait, le père entre adns le if, une fois l'exe terminer il reboucle
#fils_pid = 0 pour le processus ffils
# prog sequentiel car os.wait => cela rend le prog déterministe
#