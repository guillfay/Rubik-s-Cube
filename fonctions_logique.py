## fonctions implémentant la logique du projet : ##
## génération du cube, mélange, application des mouvements, vérifications de victoire, etc. ## 

from constantes import *

import random
import copy

# la liste FA dans constantes.py regroupe toutes les faces du cube sous forme de chaines de caractères

# on a décidé dans cet algorithme de prendre en compte les mouvements de type .'2, ce qui revient à faire .2, ce qui n'est toutefois pas évident pour un non initié
# (aussi utile pour resoudre un rubik non cubique...)
# on considère que scramble sous liste de tuple est sous la forme: [(face,' ou None,2 ou None),(....

# génère et retourne un rubik's cube résolu
# voir constantes.py pour la réprésentation
def generer_rubik_termine():
    # génère un cube entièrement noir
    cube=[[[(CO[0]*3) for j in range (TAILLE)] for k in range (TAILLE)] for l in range (TAILLE)]
    # on parcours chaque ligne de chaque face du cube et on change la couleur de chaque face de chaque cublet
    if TAILLE==3:
        # création de la face jaune
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][0]=CO[3]+cube[k][j][0][1]+cube[k][j][0][2]
        # création de la face blanche
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][2]=CO[2]+cube[k][j][2][1]+cube[k][j][2][2]
        # création de la face verte
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][0][j]=cube[k][0][j][0]+CO[4]+cube[k][0][j][2]
        # création de la face bleue
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][2][j]=cube[k][2][j][0]+CO[1]+cube[k][2][j][2]
        # création de la face orange
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[0][k][j]=cube[0][k][j][0]+cube[0][k][j][1]+CO[5]
        # création de la face rouge
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[2][k][j]=cube[2][k][j][0]+cube[2][k][j][1]+CO[6]

   
    if TAILLE==2:
        # création de la face jaune
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][0]=CO[3]+cube[k][j][0][1]+cube[k][j][0][2]
        # création de la face blanche
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][1]=CO[2]+cube[k][j][1][1]+cube[k][j][1][2]
        # création de la face verte
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][0][j]=cube[k][0][j][0]+CO[4]+cube[k][0][j][2]
        # création de la face bleue
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][1][j]=cube[k][1][j][0]+CO[1]+cube[k][1][j][2]
        # création de la face orange
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[0][k][j]=cube[0][k][j][0]+cube[0][k][j][1]+CO[5]
        # création de la face rouge
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[1][k][j]=cube[1][k][j][0]+cube[1][k][j][1]+CO[6]

    if TAILLE==4:
        # création de la face jaune
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][0]=CO[3]+cube[k][j][0][1]+cube[k][j][0][2]
        # création de la face blanche
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][j][3]=CO[2]+cube[k][j][3][1]+cube[k][j][3][2]
        # création de la face verte
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][0][j]=cube[k][0][j][0]+CO[4]+cube[k][0][j][2]
        # création de la face bleue
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[k][3][j]=cube[k][3][j][0]+CO[1]+cube[k][3][j][2]
        # création de la face orange
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[0][k][j]=cube[0][k][j][0]+cube[0][k][j][1]+CO[5]
        # création de la face rouge
        for k in range (TAILLE):
            for j in range (TAILLE):
                cube[3][k][j]=cube[3][k][j][0]+cube[3][k][j][1]+CO[6]
    return(cube)



# genere un rubik aleatoire
# nb_mouvs : nombre de mouvements aléatoires à appliquer
# retourne un tuple (rubik, scramble) (rubik : le cube généré, scramble : liste de tuples des mouvements effectués)
def generer_rubik(nb_mouvs):
    # on génère un rubiks cube terminé auquel on va appliquer des mouvements aléatoires
    rubik=generer_rubik_termine()
    # on crée une liste qui va recevoir les tuples de mouvements, et une str qui va recevoir les mouvements en str
    scramble=[]
    for i in range (nb_mouvs):
        # on crée un tuple de mouvement aléatoire: face, sens, double
        a=FA[random.randint(0,len(FA)-1)]
        b=random.choice((True,False))
        c=random.choice((True,False))
        mouv=(a,b,c)
        # on ajoute le tuple de chaque tuple du mouvement à la liste scramble, et chaque str à la liste ms
        scramble.append(mouv)
    # on applique les mouvements au rubik
    rubik=m(rubik, scramble)
    return(rubik,scramble)

# genere un rubik mélangé grâce au scramble en paramètre
# scramble : une cdc des mouvements à effectuer (par exemple "B2F2F'L2B")

def generer_rubik_scramble(scramble):	
    # on génère un rubiks cube terminé que l'on va mélanger
    rubik=generer_rubik_termine()
    # on transforme la str en liste de tuples
    scramble=mouvements(scramble)
    # on applique les mouvements au cube
    rubik=m(rubik,scramble)
    return rubik # on ne renvoie que rubik, ce qui permet d'économiser une variable dans le projet
    
# applique au rubik en paramètre nb_mouvs mouvements aléatoires
# retourne le scramble (liste de tuples des mouvements effectués)
def melanger(rubik,nb_mouvs):
    # on crée une liste qui va recevoir les tuples de mouvements, et une qui va recevoir les mouvements
    scramble=[]
    for i in range (nb_mouvs):
        # on crée un tuple de mouvement aléatoire: face, sens, double
        a=FA[random.randint(0,len(FA)-1)]
        b=random.choice((True,False))
        c=random.choice((True,False))
        mouv=(a,b,c)
        # on ajoute le tuple de chaque mouvement à la liste scramble
        scramble.append(mouv)
    # on applique le mouvement au rubik
    rubik=m(rubik, scramble)

    return (scramble)
    # on retourn seulement scramble car rubik doit etre récupéré par une autre varaible
        
    
# retourne la couleur du cubelet correspondante à la face demandée
# exemple : ("YGO", "U") renvoie "Y"
def c(cubelet,f):
    # on cherche la face du cublet désirée selon l'ordre de priorité	
    if TAILLE==3:
        if f=='U' or f=='D':
            return cubelet[0]
        if f=='F' or f=='B':
            return cubelet[1]
    if TAILLE==4:
        if f=='U' or f=='D' or f=='U1' or f=='D1':
            return cubelet[0]
        if f=='F' or f=='B' or f=='F1' or f=='B1':
            return cubelet[1]

    return cubelet[2]


# les fonctions suivantes permettent d'extraire une face du rubik en paramètre
# la face retournée, une matrice à deux dimensions, est ordonnée comme si le rubik avait été déplié
# f : lettre de la face à extraire, f = caractère (U,L,F,R,B,D)
# note : ces fonctions ne modifient PAS l'orientation (couleur) des cubelets
def extraire(rubik, f):
    ancienneface=[]
    # on copie la face que l'on souhaite extraire, en considérant qu'elle soit une face 'F'
    if TAILLE==3:
        if f=='F':
            ancienneface=[[rubik[x][0][z] for z in range(TAILLE)] for x  in range (TAILLE)]
        if f =='B':
            ancienneface=[[rubik[x][2][z] for z in range(TAILLE)] for x  in range (TAILLE-1,-1,-1)]
        if f=='L':
            ancienneface=[[rubik[0][y][z] for z in range(TAILLE)] for y  in range (TAILLE-1,-1,-1)]
        if f=='R':
            ancienneface=[[rubik[2][y][z] for z in range(TAILLE)] for y  in range (TAILLE)]
        if f=='D':
            ancienneface=[[rubik[x][y][0] for y in range(TAILLE-1,-1,-1)] for x  in range (TAILLE)]
        if f=='U':
            ancienneface=[[rubik[x][y][2] for y in range(TAILLE)] for x  in range (TAILLE)]
    if TAILLE==2:
        if f=='F':
            ancienneface=[[rubik[x][0][z] for z in range(TAILLE)] for x  in range (TAILLE)]
        if f =='B':
            ancienneface=[[rubik[x][1][z] for z in range(TAILLE)] for x  in range (TAILLE-1,-1,-1)]
        if f=='L':
            ancienneface=[[rubik[0][y][z] for z in range(TAILLE)] for y  in range (TAILLE-1,-1,-1)]
        if f=='R':
            ancienneface=[[rubik[1][y][z] for z in range(TAILLE)] for y  in range (TAILLE)]
        if f=='D':
            ancienneface=[[rubik[x][y][0] for y in range(TAILLE-1,-1,-1)] for x  in range (TAILLE)]
        if f=='U':
            ancienneface=[[rubik[x][y][1] for y in range(TAILLE)] for x  in range (TAILLE)]
    if TAILLE==4:
        if f=='F':
            ancienneface=[[rubik[x][0][z] for z in range(TAILLE)] for x  in range (TAILLE)]
        if f=='F1':
            ancienneface=[[rubik[x][1][z] for z in range(TAILLE)] for x  in range (TAILLE)]
        if f =='B':
            ancienneface=[[rubik[x][3][z] for z in range(TAILLE)] for x  in range (TAILLE-1,-1,-1)]
        if f =='B1':
            ancienneface=[[rubik[x][2][z] for z in range(TAILLE)] for x  in range (TAILLE-1,-1,-1)]
        if f=='L':
            ancienneface=[[rubik[0][y][z] for z in range(TAILLE)] for y  in range (TAILLE-1,-1,-1)]
        if f=='L1':
            ancienneface=[[rubik[1][y][z] for z in range(TAILLE)] for y  in range (TAILLE-1,-1,-1)]
        if f=='R':
            ancienneface=[[rubik[3][y][z] for z in range(TAILLE)] for y  in range (TAILLE)]
        if f=='R1':
            ancienneface=[[rubik[2][y][z] for z in range(TAILLE)] for y  in range (TAILLE)]
        if f=='D':
            ancienneface=[[rubik[x][y][0] for y in range(TAILLE-1,-1,-1)] for x  in range (TAILLE)]
        if f=='D1':
            ancienneface=[[rubik[x][y][1] for y in range(TAILLE-1,-1,-1)] for x  in range (TAILLE)]
        if f=='U':
            ancienneface=[[rubik[x][y][3] for y in range(TAILLE)] for x  in range (TAILLE)]
        if f=='U1':
            ancienneface=[[rubik[x][y][2] for y in range(TAILLE)] for x  in range (TAILLE)]

    

    return(ancienneface)

    
# applique une rotation à la face passée en paramètre
# cette fonction ne modifie PAS l'orientation (couleur) des cubelets
# face : matrice 2D de cubelets
# sens : True pour horaire
# double : True pour 180°
def appliquer_rotation(face, sens, double): ###ATT /!!!\ JAI ENLEVE LA COPIE DE LA FACE SI MOUV PAS DOUBLE
    # on effectue un mouvement de rotation de type 'F' pour la face suivant les paramètres sens et double
    if double==True:
        nouv=face # on copie la face afin de la garder en memoire, et on modifie nouv
        for i in range(2):
            # on fait deux fois le mouvement
            nouv=[[nouv[x][z] for x in range(TAILLE)] for z in range (TAILLE-1,-1,-1)]
        return nouv
    if sens==False and double==False:
        face=[[face[x][z] for x in range(TAILLE)] for z in range (TAILLE-1,-1,-1)] # on écrase la face en la faisant tourner
        return face
    elif sens==True and double==False:
        face=[[face[x][z] for x in range(TAILLE-1,-1,-1)] for z in range (TAILLE)] # idem dans le sens opposé
        return face



# reimplante (remplace) la face f de rubik avec les cubelets du paramètre face
# note : cette fonction n'applique PAS de rotation ou de réorientation des cubelets
# f : lettre de la face à remplacer, f = caractère (U,L,F,R,B,D)
# face : matrice 2D de cubelets
def reimplanter(rubik, f, face):
    # pour chaque face du rubik, selon sa nature, on remplace un à un chaque cublet indépendamment de son orientation par la nouvelle face à changer
    if TAILLE==3:
        if f=='F':
            for x in range(TAILLE):
                for z in range (TAILLE):
                    rubik[x][0][z]=face[x][z]
        if f=='B':
            for x in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[x][2][z]=face[2-x][z]
        if f=='L':
            for y in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[0][y][z]=face[2-y][z]
        if f=='R':
            for y in range (TAILLE):
                for z in range (TAILLE):
                    rubik[2][y][z]=face[y][z]
        if f=='D':
            for x in range (TAILLE):
                for y in range(TAILLE-1,-1,-1):
                    rubik[x][y][0]=face[x][2-y]
        if f=='U':
            for x in range (TAILLE):
                for y in range(TAILLE):
                    rubik[x][y][2]=face[x][y]

    if TAILLE==2:
        if f=='F':
            for x in range(TAILLE):
                for z in range (TAILLE):
                    rubik[x][0][z]=face[x][z]
        if f=='B':
            for x in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[x][1][z]=face[1-x][z]
        if f=='L':
            for y in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[0][y][z]=face[1-y][z]
        if f=='R':
            for y in range (TAILLE):
                for z in range (TAILLE):
                    rubik[1][y][z]=face[y][z]
        if f=='D':
            for x in range (TAILLE):
                for y in range(TAILLE-1,-1,-1):
                    rubik[x][y][0]=face[x][1-y]
        if f=='U':
            for x in range (TAILLE):
                for y in range(TAILLE):
                    rubik[x][y][1]=face[x][y]

    if TAILLE==4:
        if f=='F':
            for x in range(TAILLE):
                for z in range (TAILLE):
                    rubik[x][0][z]=face[x][z]
        if f=='F1':
            for x in range(TAILLE):
                for z in range (TAILLE):
                    rubik[x][1][z]=face[x][z]
        if f=='B':
            for x in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[x][3][z]=face[3-x][z]
        if f=='B1':
            for x in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[x][2][z]=face[3-x][z]
        if f=='L':
            for y in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[0][y][z]=face[3-y][z]
        if f=='L1':
            for y in range(TAILLE-1,-1,-1):
                for z in range(TAILLE):
                    rubik[1][y][z]=face[3-y][z]
        if f=='R':
            for y in range (TAILLE):
                for z in range (TAILLE):
                    rubik[3][y][z]=face[y][z]
        if f=='R1':
            for y in range (TAILLE):
                for z in range (TAILLE):
                    rubik[2][y][z]=face[y][z]
        if f=='D':
            for x in range (TAILLE):
                for y in range(TAILLE-1,-1,-1):
                    rubik[x][y][0]=face[x][3-y]
        if f=='D1':
            for x in range (TAILLE):
                for y in range(TAILLE-1,-1,-1):
                    rubik[x][y][1]=face[x][3-y]
        if f=='U':
            for x in range (TAILLE):
                for y in range(TAILLE):
                    rubik[x][y][3]=face[x][y]
        if f=='U1':
            for x in range (TAILLE):
                for y in range(TAILLE):
                    rubik[x][y][2]=face[x][y]
    return (rubik)


# effectue un mouvement du rubik
# extrait, applique la rotation, réoriente les couleurs et réimplante la face
# mouv est un tuple (f, sens, double)
# f = caractère (U,L,F,R,B,D)
# sens = booleen (True = horaire)
# double = boolean (True = 180°)

def appliquer_mouvement(rubik, mouv):
    # on extrait la face pour laquelle il faut effecteur le mouvement
    face_extraite=extraire(rubik,mouv[0])
    # on effectue la rotation de la face extraite
    nouvelle_face=appliquer_rotation(face_extraite,mouv[1],mouv[2])
    # on réoriente les faces des cublets
    for i in range(TAILLE):
        for j in range(TAILLE):
            # pour chaque type de mouvement (face et sens), on crée une liste du cublet que l'on met dans l'ordre (selon la priorité de l'énoncé) et que l'on réimplémente sous forme de str
            if mouv[0]=='F' or mouv[0]=='B' or mouv[0]=='F1' or mouv[0]=='B1':
                a=list(nouvelle_face[i][j])
                if mouv[2]==False:
                    nouvelle_face[i][j]=a[2]+a[1]+a[0]
                else:
                    nouvelle_face[i][j]=a
            if mouv[0]=='L' or mouv[0]=='R' or mouv[0]=='L1' or mouv[0]=='R1':
                a=list(nouvelle_face[i][j])
                if mouv[2]==False:
                    nouvelle_face[i][j]=a[1]+a[0]+a[2]
                else:
                    nouvelle_face[i][j]=a
            if mouv[0]=='D' or mouv[0]=='U' or mouv[0]=='D1' or mouv[0]=='U1':
                a=list(nouvelle_face[i][j])
                if mouv[2]==False:
                    nouvelle_face[i][j]=a[0]+a[2]+a[1]
                else:
                    nouvelle_face[i][j]=a
    # on réimplémente la face ayant subit une rotation dans le rubik
    rubik = reimplanter(rubik,mouv[0],nouvelle_face)
    # on retourne le rubik ainsi modifié
    return rubik
    
# renvoie True si la face est terminée
# face : matrice 2D de cubelets
# f : caractère (U,L,F,R,B,D)
def face_terminee(face,f):
    # on compare la face en question à la face d'un cube terminé
    face_terminee=extraire(generer_rubik_termine(),f)
    if face==face_terminee:
        return True
    return False

    
# renvoie True si le cube est terminé
def victoire(rubik):
    # on compare le rubik au terme de ses modifications à un cube "neuf"
    if rubik==generer_rubik_termine():
        return True
    return False
    
# renvoie un tuple (face, sens, double) correspondant au mouvement m
# m : chaîne de caractères représentant un mouvement
# exemples: "F" renvoie ('F',True,False), "R'" renvoie ('R',False,False), "L2" renvoie ('L',False,True)
# m DOIT être valide
def mouv(m):
    if len(m)==1:
        mvt=(m[0],True,False)
    if len(m)==2:
        if m[1]=='2':
            mvt=(m[0],True,True)
        else:
            mvt=(m[0],False,False)
    if len(m)==3:
        mvt=(m[0],False,True)
    # TODO	
    return mvt

# renvoie une liste de tuples correspondants aux mouvements ms
# ms : chaîne de caractères représentant des mouvements (scramble)
# exemple: "F R' L2" renvoie [('F',True,False),('R',False,False),('L',False,True)]
# ms DOIT être valide
def mouvements(ms):  
     # on considère des mouvements sans espaces entre eux et que ms n'a pas à être vérifié    
     # on crée une liste qui va recevoir dans un premier temps les chaines de caractère des mouvements isolés, puis des tuples valides
     l=[]
     if len(ms)==1:
          # on vérifie dans ce cas que l'utilisateur a bien rentré une face
          if ms[0] in FA:
               l.append(ms[0])
     if len(ms)==2:
          # on vérifie que l'utilisateur a bien renseigné une face en premier
          if ms[0] in FA:
               # puis un sens
               if ms[1]=="'":
                    l.append(ms[0]+ms[1]) 
               # ou un double  
               if ms[1]=="2":
                    l.append(ms[0]+ms[1])
               # ou un deuxième mouvement de face
               if ms[1] in FA:
                    l.append(ms[0])
                    l.append(ms[1])
     # si la saisie de mouvement contient plus de 2 termes, alors il y a une condition d'arret à respecter
     i=0 # parcourt la chaine de caractère saisie par l'utilisateur
     c='"'  # variable provisoire recevant la chaine de caractère de chaque mouvement isolé
     while i<len(ms)-2: # on s'arrête deux termes avant la fin de la saisie
          # on cherche à parcourir la liste afin d'isoler les chaines de caractère de chaque mouvement
          if ms[i] in FA: 
               if ms[i+1]=="'":
                    if ms[i+2]=="2":
                         c=ms[i:i+3]
                         l.append(c) # on ajoute le mouvement à la liste
                    else:
                         c=ms[i:i+2]
                         l.append(c)
               elif ms[i+1]=="2":
                    c=ms[i:i+2]
                    l.append(c)
               elif ms[i+1]!="'" and ms[i+1]!="2":
                    c=ms[i]
                    l.append(c)
          i+=len(c)  # len(c) désigne la longueur du mouvement élémentaire isolé et le compteur de la boucle i est incrémenté de façon à ce que ms[i] soit toujours, si la saisie est correcte, une face
     r=len(ms)-i # c'est ce qui reste à parcourir de la saisie utilisateur

           
     if r==2 and i!=0:   # s'il reste 2 éléments dans la chaine de caractère, mais que l'on a parcouru la boucle (conflit avec le deuxieme "if" de la fonction)       
          if ms[len(ms)-2] in FA: # on procède de la même façon en vérifiant face-face, face-sens, face-double
               if ms[len(ms)-1]=="'" or ms[len(ms)-1]=="2":
                    l.append(ms[len(ms)-2]+ms[len(ms)-1])
               if ms[len(ms)-1] in FA:
                    l.append(ms[len(ms)-2])
                    l.append(ms[len(ms)-1])
     # la liste l contient maintenant uniquement des chaines de caractères de mouvement isolés et vaildes, il suffit de les décomposer en tuples (face,sens,double)
     for k in range (len(l)):
          if len(l[k])==1: # c'est forcément une face
              l[k]=(l[k][0],True,False)
          elif len(l[k])==2 and l[k][1]=="'": # cas face-sens
              l[k]=(l[k][0],False,False)
          elif len(l[k])==2 and l[k][1]=="2": # cas face-double
              l[k]=(l[k][0],True,True)
          elif len(l[k])==3: # cas face-sens-double
              l[k]= (l[k][0],False,True)
     return l
     # on retourne le mouvement valide sous forme de liste de tuples de mouvements élémentaires sous forme (face, sens, double)
     # on retourne le mouvement valide sous forme de liste de tuples de mouvements élémentaires sous forme (face, sens, double)

    
# applique les mouvements ms au cube rubik
# ms : chaîne de caractères représentant des mouvements (scramble)
def m(rubik, ms):
    if type(ms) is str: # on convertit la str en liste: cette fonction peut recevoir directement la liste de tuples ou convertir la str comme telle
        mvt=mouvements(ms)
    else:
        mvt=ms
    # pour chaque mouvement élémentaire de la liste ms, on applique le mouvement au rubik, que l'on renvoie une fois tous les mouvements appliqués
    for k in mvt:
        rubik=appliquer_mouvement(rubik,k)
    for x in range (TAILLE):
        for y in range (TAILLE):
            for z in range (TAILLE):
                rubik[x][y][z]="".join(rubik[x][y][z])
    return rubik
    
# renvoie une chaîne de caractères correspondant aux mouvements mouvs
# exemple: [('F',True,False),('R',False,False),('L',False,True)] renvoie "F R' L'2" ==> par choix, je ne renvoie pas de str avec des espaces
def scramble(mouvs):
    # on crée une str qui va recevoir tous les mouvements sous forme de str
    s=""
    # on parcourt la liste mouvs
    for k in mouvs:
        # on parcourt chaque tuple de l'élément de la liste
        # on ajoute à la str l'élément de mouvement correspondant
        s+=k[0]
        if k[1]==False:
            s+="'"
        if k[2]==True:
            s+="2"
    # on renvoie la chaine de caractère contenant les mouvements accolés
    return s
    
    
