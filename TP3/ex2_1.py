import os, sys

# wc affiche ligne mot octet d'un fichier 
# sort affiche les lignes d'un fichier dans l'ordre demander -n pour les numerique
# grep resssort le nombre d'occurance d'un mot dans un fichier
# | pipe d'instruction l'instuction suivante se fait sur le résultat de la précedente
'''
command = [
    ["/bin/cat", ["cat","prenom.txt | wc"]],
    ["/usr/bin/sort", ["sort","< ex1.py | grep chaine | tail -n 5 > sortie"]]
]'''

(dfr,dfw) = os.pipe() 
pid = os.fork()

if pid != 0:
    os.close(dfr)
    os.dup2(dfw,1)
    os.close(dfw)
    os.execlp("cat", "cat","ex1.py")

else:
    os.close(dfw)
    os.dup2(dfr,0)
    os.close(dfr)
    os.execlp("wc","wc")