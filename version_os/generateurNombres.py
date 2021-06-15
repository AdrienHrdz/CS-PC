import sys
import os
from random import randint

#programme prend en argument N, dfwPAIR, dfwIMPAIR dans cet ordre exactement
#N : Nombre d'éléments aléatoires à generer
#dfwPAIR : Pipe en écriture pour les nombres pairs
#dfwIMPAIR : Pipe en lecture pour les nombres impairs

#====================
# Initialisation
#====================

#Attribution des arguments
N = int(sys.argv[1])
dfwPAIR = int(sys.argv[2])
dfwIMPAIR = int(sys.argv[3])

#Autres variables
a = 0
b = 9



#====================
# Début du programme
#====================

#Génération des nombres et envoie dans le pipe adéquat
for i in range(N):

	val = randint(a,b) #Generation du nombre aléatoire
	strval = str(val)
	strval = strval.encode("ascii") #Conversion de ce nombre pour pouvoir le mettre dans le pipe

	if val%2 == 0: #Le nombre est pair
		os.write(dfwPAIR,strval) #On le dépose dans le pipe pair
	else:#Sinon
		os.write(dfwIMPAIR,strval) #On le dépose dans le pipe impair

#On dépose la valeur -1 dans les deux tubes
fin = str(-1)
fin = fin.encode("ascii")
os.write(dfwPAIR,fin)
os.write(dfwIMPAIR,fin)

#On ferme les pipes
os.close(dfwPAIR)
os.close(dfwIMPAIR)

sys.exit(0)







