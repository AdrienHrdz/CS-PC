#LIBRAIRIES
import random
from time import time
import multiprocessing as mp

#FONCTIONS
# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
def frequence_de_hits_pour_n_essais(sem,nb_iteration):
	count = 0
	for i in range(nb_iteration):
		x = random.random()
		y = random.random()

		# si le point est dans l’unit circle
		if x * x + y * y <= 1: 
			count += 1
	
	sem.acquire() #Cette phase permet au process d'ajouter sa valeur de count dans la variable global sans erreurs (dans le cas ou deux process voudraient le faire au même moment)
	nb_hits.value += count
	sem.release()

#PROGRAMME
time_start = time()
nb_processus = 16

#Nombre d’essais pour l’estimation
nb_total_iteration = 10000000
nb_iteration_par_process = nb_total_iteration/nb_processus

#Création de la mêmoire partagée
nb_hits = mp.Value("i",0)
#Création du sémaphore
sem = mp.Semaphore(1)
#Création des processus et mise en route
if __name__ =='__main__':
	liste_process = []
	for i in range(nb_processus):
		liste_process.append(mp.Process(target=frequence_de_hits_pour_n_essais, args=(sem,int(nb_iteration_par_process))))
		liste_process[i].start()

	for i in range(nb_processus):
		liste_process[i].join()

	print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits.value / nb_total_iteration)
	time_end = time()
	total_time_mono = time_end - time_start
	print("Temps de calculs ",total_time_mono," secondes")

#TRACE :
# Calcul Mono−Processus : Valeur estimée Pi par la méthode Mono−Processus : 3.1412604
# Dans cette situation, il faut en moyenne 0.2 secondes pour calculer à 10-3 près avec 10 000 000 d'itérations (avec 8 processus)


