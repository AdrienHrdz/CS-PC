import sys
import os

#programme prend en argument dfr, dfw dans cet ordre exactement
#dfr : lecture du générateur de nombres
#dfw : ecriture dans le pipe de la somme

#====================
# Initialisation
#====================

#Attribution des arguments
dfr = int(sys.argv[1])
dfw = int(sys.argv[2])


#====================
# Début du programme
#====================
msgRecu = os.read(dfr,1)
msgRecu = msgRecu.decode("ascii")
Somme = msgRecu

while msgRecu != -1:
	msgRecu = os.read(dfr,1)
	msgRecu = msgRecu.decode("ascii")
	Somme += msgRecu

os.write(dfw,Somme)

os.close(dfw)

sys.exit(0)

	
