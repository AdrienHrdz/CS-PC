import os
import sys

#Pour executer le programme depuis la fenetre de commande : python3 main.py

#Notes : problème récurrent à la lecture dans un pipre >> OSError: [Errno 9] Bad file descriptor
#Pourtant les éléments spécifié dans le os.read(id_pipe_r,taille_message) sont correctement spécifié
#La taille des messages est paramétré à 1 car les nombres sont générés de 0 à 9. Leur conversion en ASCII fait qu'ils ont une longueur d'un byte. 

#====================
# Initialisation 
#====================
#variables du programme
N=10 #Nombre d'éléments à sommer

#Création des pipes
(dfrPAIR,dfwPAIR) = os.pipe()
(dfrIMPAIR,dfwIMPAIR) = os.pipe()
(dfrSOMMEPAIR,dfwSOMMEPAIR) = os.pipe()
(dfrSOMMEIMPAIR,dfwSOMMEIMPAIR) = os.pipe()

#====================
# Début du programme
#====================
#Génération des processus avec la librairie os
pid_gen = os.fork()
if pid_gen == 0: #Premier fils generation des nombres
	os.execlp("python3","python3","generateurNombres.py",str(N),str(dfwPAIR),str(dfwIMPAIR))
else :
	os.close(dfwPAIR)
	os.close(dfwIMPAIR)
	pidpair = os.fork()
	if pidpair == 0: #Deuxieme fils reception des nombres paires et somme
		os.execlp("python3","python3","somme.py",str(dfrPAIR), str(dfwSOMMEPAIR))
	else :
		os.close(dfrPAIR)
		os.close(dfwSOMMEPAIR)
		pidpair = os.fork()
		if pidpair == 0: #Troisieme fils reception des nombres impaires et somme
			os.execlp("python3","python3","somme.py",str(dfrIMPAIR), str(dfwSOMMEIMPAIR))

os.close(dfrIMPAIR)
os.close(dfwSOMMEIMPAIR)

#Le père reçoit les sommes paires et impaires et fait l'affichage
val_recu = os.read(dfrSOMMEPAIR,1)
Somme = val_recu.decode("ascii")
os.close(dfrSOMMEPAIR)

val_recu = os.read(dfrSOMMEIMPAIR,1)
Somme += val_recu.decode("ascii")
os.close(dfrSOMMEIMPAIR)

print("La somme est de : ", Somme)
sys.exit(0)
