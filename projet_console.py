## le projet Rubik en interaction console (script executable) ##

from constantes import *
from fonctions_logique import *
from fonctions_console import *

##############################################
# une fonction qui permet de saisir un entier et demande à l'utilisateur de recommencer tant qu'il se trompe
def saisirentier():
    a=input("Saisir un nombre de mouvements à effectuer (entier): ")
    try:
        int(a)
        return int(a)
    except ValueError:
        print("Ce n' est pas un entier: ")
        return(saisirentier())
############################################## on définit des fonctions selon les cas de figures
def oui(rubik):
    # demandons maintenant à l'utilisateur de donner des mouvements à effectuer à un rubiks cube neuf
    # il entre une suite de mouvements
    print("On mélange le cube: ")
    suite_mouv=saisie_mouvements()
    print(suite_mouv)
    # on applique cette suite de mouvements
    rubik=m(rubik,suite_mouv)
    # on affiche ce cube
    print("Cube mélangé par l'utilisateur: ")
    afficher_rubik(rubik)
    # on affiche les mouvements que l'utilisateur a donné (en rappel...)
    print("Mouvements effectués: ")
    print(scramble(suite_mouv))

def non(rubik):
    print("Cube 'neuf' déplié: ")
    afficher_rubik(rubik)

def aleatoire(rubik):
    # on mélange aléatoirement un NOUVEAU cube mélangé avec  un nombre de mouvements aléatoires défini par l'utilisateur
    nb_mouvs=saisirentier()
    rubik=generer_rubik(nb_mouvs)
    # on affiche le cube mélangé ainsi que les mouvements effectués
    print("Rubik mélangé aléatoirement: ")
    afficher_rubik(rubik[0])
    # ces mouvements sont sous forme de chaine de caractère
    mouv_appliqués=scramble(rubik[1])
    print("Mouvements effectués: ")
    print(mouv_appliqués)
    # le rubiks cube est maintenant mélangé avec une suite de mouvements connus
    # les fonctions generer_rubik_scramble et melanger sont basees sur generer_rubik et ne sont pas testées ici

def interaction(rubik):
    # on demande à l'utilisateur s'il souhaite réaliser des mouvements
    choix=input("Voulez vous mélanger le cube? 'non', 'aléatoire','oui','recommencer avec un cube neuf','stop': ")
    # en fonction de ses choix, des modifications sont faites sur le cube
    if choix=="non":
        print(non(rubik))
        return interaction((rubik))

    if choix=="aléatoire":
        print(aleatoire(rubik))
        return interaction((rubik))

    if choix=="oui":
        print(oui(rubik))
        return interaction((rubik))

    if choix=='recommencer avec un cube neuf':
        rubik=generer_rubik_termine()
        print("Cube 'neuf' déplié: ")
        afficher_rubik(rubik)
        return interaction(rubik)

    if choix=='stop':
        print("Merci d'avoir joué! :)")

    else:
        print("Votre saisie n'est pas valide, recommncez")
        return interaction(rubik)
############################################################

# on commence par définir un cube non mélangé
rubik=generer_rubik_termine()

# on peut afficher ce cube
print("Cube 'neuf' déplié: ")
afficher_rubik(rubik)

# on lance l'interaction avec l'utilisateur
print(interaction(rubik))




