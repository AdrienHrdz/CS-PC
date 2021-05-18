import sys

if len(sys.argv) == 1 :
    print("Pas de moyenne à calculer")
    sys.exit()
Somme = 0
for arg in sys.argv[1:]:
    
    if arg.isnumeric() == True:
        note = float(arg)
        if (note >= 0) and (note <= 20):
            Somme += note
        else:
            print("Erreur : Note(s) non valide(s)")
            sys.exit()
    else:
        print("Erreur : Note(s) non valide(s)")
        sys.exit()

moyenne  = Somme/(len(sys.argv)-1)
print("Moyenne est : ", "%.2f" %moyenne)
sys.exit()