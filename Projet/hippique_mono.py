# Cours hippique
# Version très basique, sans mutex sur l’écran, sans arbitre, sans annoncer le gagant, ... ...
# Quelques codes d’échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"
# Clear SCReen
CLEAREOS = "\x1B[J"
# Clear End Of Screen
CLEARELN = "\x1B[2K"
# Clear Entire LiNe
CLEARCUP = "\x1B[1J"
# Clear Curseur UP
GOTOYX = "\x1B[%.2d;%.2dH"
# (’H’ ou ’f’) : Goto at (y,x), voir le code
DELAFCURSOR = "\x1B[K"
# effacer après la position du curseur
CRLF = "\r\n"
# Retour à la ligne
# VT100 : Actions sur le curseur
CURSON = "\x1B[?25h"
# Curseur visible
CURSOFF = "\x1B[?25l"
# Curseur invisible
# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"
# Normal
BOLD = "\x1B[1m"
# Gras
UNDERLINE = "\x1B[4m"
# Souligné
# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"
# Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"
# Rouge
CL_GREEN="\033[22;32m"
# Vert
CL_BROWN = "\033[22;33m"
# Brun
CL_BLUE="\033[22;34m"
# Bleu
CL_MAGENTA="\033[22;35m"
# Magenta
CL_CYAN="\033[22;36m"
# Cyan
CL_GRAY="\033[22;37m"
# Gris
# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"
# Gris foncé
CL_LIGHTRED="\033[01;31m"
# Rouge clair
CL_LIGHTGREEN="\033[01;32m"
# Vert clair
CL_YELLOW="\033[01;33m"
# Jaune
CL_LIGHTBLU= "\033[01;34m"
# Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"
# Magenta clair
CL_LIGHTCYAN="\033[01;36m"
# Cyan clair
CL_WHITE="\033[01;37m"
# Blanc
#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# Juin 2019
# Cours hippique
# Version très basique, sans mutex sur l’écran, sans arbitre, sans annoncer le gagant, ... ...
# Quelques codes d’échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"
# Clear SCReen
CLEAREOS = "\x1B[J"
# Clear End Of Screen
CLEARELN = "\x1B[2K"
# Clear Entire LiNe
CLEARCUP = "\x1B[1J"
# Clear Curseur UP
GOTOYX = "\x1B[%.2d;%.2dH"
# (’H’ ou ’f’) : Goto at (y,x), voir le code
DELAFCURSOR = "\x1B[K"
# effacer après la position du curseur
CRLF = "\r\n"
# Retour à la ligne
# VT100 : Actions sur le curseur
CURSON = "\x1B[?25h"
# Curseur visible
CURSOFF = "\x1B[?25l"
# Curseur invisible
# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"
# Normal
BOLD = "\x1B[1m"
# Gras
UNDERLINE = "\x1B[4m"
# Souligné
# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"
# Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"
# Rouge
CL_GREEN="\033[22;32m"
# Vert
CL_BROWN = "\033[22;33m"
# Brun
CL_BLUE="\033[22;34m"
# Bleu
CL_MAGENTA="\033[22;35m"
# Magenta
CL_CYAN="\033[22;36m"
# Cyan
CL_GRAY="\033[22;37m"
# Gris
#4Exercices à réaliser
# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"
# Gris foncé
CL_LIGHTRED="\033[01;31m"
# Rouge clair
CL_LIGHTGREEN="\033[01;32m"
# Vert clair
CL_YELLOW="\033[01;33m"
# Jaune
CL_LIGHTBLU= "\033[01;34m"
# Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"
# Magenta clair
CL_LIGHTCYAN="\033[01;36m"
# Cyan clair
CL_WHITE="\033[01;37m"
# Blanc
#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
from multiprocessing import Process
import os, time,math, random, sys, ctypes
import multiprocessing as mp

LONGEUR_COURSE = 10 # Tout le monde aura la même copie (donc no need to have a ’value’)
keep_running=mp.Value(ctypes.c_bool, True)

# Une liste de couleurs à affecter aléatoirement aux chevaux
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
    CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN, CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]

def effacer_ecran() : print(CLEARSCR,end="")
def erase_line_from_beg_to_curs() : print("\033[1K",end="")
def curseur_invisible() : print(CURSOFF,end="")
def curseur_visible() : print(CURSON,end="")
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end="")

def en_couleur(Coul) : print(Coul,end="")
def en_rouge() : print(CL_RED,end="") # Un exemple !


# La tache d’un cheval
def un_cheval(ma_ligne : int,lock,col) : # ma_ligne commence à 0
    je_flote = 3*ma_ligne
    while col[ma_ligne] < LONGEUR_COURSE and keep_running.value :

        lock.acquire() #On met le mutex ici pour ne pas que le curseur de la console bouge pendant qu'un autre veut le bouger
        move_to(je_flote+1,col[ma_ligne])
        # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[je_flote%len(lyst_colors)])
        print("   _   ")
        move_to(je_flote+2,col[ma_ligne])
        erase_line_from_beg_to_curs()
        print("__(.)= ")
        move_to(je_flote+3,col[ma_ligne])
        erase_line_from_beg_to_curs()
        print("\_"+chr(ord("A")+ma_ligne)+"_) ")
        lock.release()

        col[ma_ligne]+=1
        time.sleep(0.1 * random.randint(1,5))

#On définit l'arbitre

def arbitrage(col,lock,longueur_course):
    nb_process = len(col)*3
    maxi = 0
    index_max = 0
    while maxi < longueur_course :
        for i in range(nb_process):
            if col[i] > maxi:
                index_max = i
                maxi = col[i]
            if col[i] == min(col):
                index_min = i
        
        lock.acquire() #On implémente notre mutex pour eviter de bouger le curseur dans la console au moment où un autre processus le ferait
        move_to(nb_process+2,0)
        print(CLEARELN)
        en_couleur(CL_WHITE)
        print("Le cheval en tête est : ", chr(65+index_max), "; Le cannassons à la ramasse est :", chr(65+index_min))
        lock.release()
        time.sleep(0.1)

    index_win = []
    for i in range(nb_process):
        if col[i] == longueur_course:
            index_win.append(i)

    if len(index_win) == 1:
        lock.acquire() #On implémente notre mutex pour eviter de bouger le curseur dans la console au moment où un autre processus le ferait
        move_to(nb_process+5,0)
        print(CLEARELN)
        en_couleur(CL_WHITE)
        print("Le cheval gagant est : ", chr(65+index_win[0]))
        lock.release()
    
    else:
        for i in enumerate(index_win) :
            index_win[i] = chr(65+index_win[i])
        lock.acquire() #On implémente notre mutex pour eviter de bouger le curseur dans la console au moment où un autre processus le ferait
        move_to(nb_process+5,0)
        print(CLEARELN)
        en_couleur(CL_WHITE)
        print("Le cheveaux ex-eaquo sont  : ", index_win)
        lock.release()
    



    
#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
# La partie principale :
def course_hippique() :
    Nb_process=10
    mutex = mp.Lock()
    mes_process = [0 for i in range(Nb_process)]
    effacer_ecran()
    curseur_invisible()

    #On déclare un tableau partagé contenant les colonnes de chacune des lignes
    col = mp.Array('i',range(Nb_process))
    for i in col : 
        col[i]=1

    for i in range(Nb_process): # Lancer Nb_process processus
        mes_process[i] = Process(target=un_cheval, args= (i,mutex,col))
        mes_process[i].start()
    
    #On démarre l'arbitre
    arbitre = mp.Process(target=arbitrage, args=(col,mutex,LONGEUR_COURSE))
    arbitre.start()

    move_to(Nb_process+10, 1)
    print("tous lancés")


    for i in range(Nb_process): mes_process[i].join()

    move_to(24, 1)
    en_couleur(CL_WHITE)
    curseur_visible()
    print("Fini")


# La partie principale :
if __name__ == "__main__" :
    course_hippique()