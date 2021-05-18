#miroir
import sys
chaine = sys.argv[1]
print("Argument : ",chaine)
chaine_miroir = ''
for char in chaine :
    chaine_miroir = char + chaine_miroir  
print("Argument renversé : ",chaine_miroir)