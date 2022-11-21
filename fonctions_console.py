## fonctions pour l'interface utilisateur en console ##


from typing import Tuple
'''from typing_extensions import ParamSpecArgs''' # je ne sais que faire de ce module
from constantes import *
from fonctions_logique import *


# affiche un rubik en console
# le rubik est affiché en mode "déplié"
# exemple :
    # ~ WWW
    # ~ WWW
    # ~ YYY
     # ~ U

# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
# ~ OOR GGG ORR   BBB
 # ~ L   F   R     B

    # ~ WWW
    # ~ YYY
    # ~ YYY
     # ~ D
def afficher_rubik(rubik):
     if TAILLE==3:
          # on print sur chaque ligne le cube déplié
          for j in range (TAILLE-1,-1,-1): # pour la face 'U' (3 fois chaque ligne)
               l="  "*TAILLE # on ajoute des cases vides pour déplier le cube
               for n in range (TAILLE):#blanc
                    l=l+" "+rubik[n][j][2][0] # on ajoute les éléménts de la ligne
               l+="  "*2*TAILLE # on ajoute des cases vides pour représenter les 2 faces restantes du cube déplié
               print(l) # on affiche la ligne du cube déplié
          for j in range (TAILLE-1,-1,-1): # su le même principe, on affiche lles lignes du cube déplié pour chaque face :'L','F','R','B'
               l=""
               for i in range (TAILLE-1,-1,-1): # orange
                    l=l+" "+rubik[0][i][j][2]
               for k in range (TAILLE): #vert
                    l=l+" "+rubik[k][0][j][1] # on ajoute les éléménts de la ligne
               for m in range (TAILLE): #rouge
                    l=l+" "+rubik[2][m][j][2]
               for p in range (TAILLE-1,-1,-1):
                    l=l+" "+rubik[p][2][j][1]#bleu
               print(l)
          for j in range(TAILLE): # pour la face 'D' (3 fois chaque ligne)
               l="  "*TAILLE
               for k in range (TAILLE): #jaune
                    l=l+" "+rubik[k][j][0][0]
               l+="  "*2*TAILLE
               print(l)
     if TAILLE==2:
                    # on print sur chaque ligne le cube déplié
          for j in range (TAILLE-1,-1,-1): # pour la face 'U' (3 fois chaque ligne)
               l="  "*TAILLE # on ajoute des cases vides pour déplier le cube
               for n in range (TAILLE):#blanc
                    l=l+" "+rubik[n][j][1][0] # on ajoute les éléménts de la ligne
               l+="  "*2*TAILLE # on ajoute des cases vides pour représenter les 2 faces restantes du cube déplié
               print(l) # on affiche la ligne du cube déplié
          for j in range (TAILLE-1,-1,-1): # su le même principe, on affiche lles lignes du cube déplié pour chaque face :'L','F','R','B'
               l=""
               for i in range (TAILLE-1,-1,-1): # orange
                    l=l+" "+rubik[0][i][j][2]
               for k in range (TAILLE): #vert
                    l=l+" "+rubik[k][0][j][1] # on ajoute les éléménts de la ligne
               for m in range (TAILLE): #rouge
                    l=l+" "+rubik[1][m][j][2]
               for p in range (TAILLE-1,-1,-1):
                    l=l+" "+rubik[p][1][j][1]#bleu
               print(l)
          for j in range(TAILLE): # pour la face 'D' (3 fois chaque ligne)
               l="  "*TAILLE
               for k in range (TAILLE): #jaune
                    l=l+" "+rubik[k][j][0][0]
               l+="  "*2*TAILLE
               print(l)
     if TAILLE==4:
                    # on print sur chaque ligne le cube déplié
          for j in range (TAILLE-1,-1,-1): # pour la face 'U' (3 fois chaque ligne)
               l="  "*TAILLE # on ajoute des cases vides pour déplier le cube
               for n in range (TAILLE):#blanc
                    l=l+" "+rubik[n][j][3][0] # on ajoute les éléménts de la ligne
               l+="  "*2*TAILLE # on ajoute des cases vides pour représenter les 2 faces restantes du cube déplié
               print(l) # on affiche la ligne du cube déplié
          for j in range (TAILLE-1,-1,-1): # su le même principe, on affiche lles lignes du cube déplié pour chaque face :'L','F','R','B'
               l=""
               for i in range (TAILLE-1,-1,-1): # orange
                    l=l+" "+rubik[0][i][j][2]
               for k in range (TAILLE): #vert
                    l=l+" "+rubik[k][0][j][1] # on ajoute les éléménts de la ligne
               for m in range (TAILLE): #rouge
                    l=l+" "+rubik[3][m][j][2]
               for p in range (TAILLE-1,-1,-1):
                    l=l+" "+rubik[p][3][j][1]#bleu
               print(l)
          for j in range(TAILLE): # pour la face 'D' (3 fois chaque ligne)
               l="  "*TAILLE
               for k in range (TAILLE): #jaune
                    l=l+" "+rubik[k][j][0][0]
               l+="  "*2*TAILLE
               print(l)

# retourne True si le saisie est un mouvement valide
# les mouvements valides sont une chaine de caractères sous la forme (F|L|R|U|D|B['|2])
def saisie_valide(saisie):
     # saisie est un mouvement et pour chaque longueur de saisie, on regarde s'il est bien sans espace et qu'il s'enchaine sous la forme face, face-sens, face-double, face-sens-double
     if len(saisie)==1:
          for i in FA:
               if saisie[0]==i:
                    return True
     if len(saisie)==2:
          for i in FA:
               if saisie[0]==i and (saisie[1]=="'" or saisie[1]=='2'):
                    return True
     if len(saisie)==3:
          for i in FA:
               if saisie[0]==i and saisie[1]=="'" and saisie[2]=='2':
                    return True
     return False
     
     
     
# permet la saisie d'un mouvement à effectuer
# sous la forme (F|L|R|U|D|B['|2])
# lettre = face
# ' = anti-horaire
# 2 = 180°				
# renvoie toujours un tuple valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvement():
     # on demande à l'utilisateur de saisir un unique mouvement
     prop=input("Donner un mouvement à effectuer sous la forme (F|L|R|U|D|B['|2]): ")
     while saisie_valide(prop)==False:
          # tant que le mouvement n'est pas valide (cf fonction ci-dessus), l'utilisateur doit recommencer sa saisie
          prop=input("Donner un mouvement correct à effectuer sous la forme (F|L|R|U|D|B['|2]): ")
     # selon la longueur de chaque mouvement, on crée un tuple qui contient les nformations du mouvement sous la forme (face, sens, double)
     if len(prop)==1:
          return (prop[0],True,False)
     if len(prop)==2 and prop[1]=="'":
          return (prop[0],False,False)
     if len(prop)==2 and prop[1]=="2":
          return (prop[0],True,True)
     else:
          return (prop[0],False,True)
          # si on ne passe dans aucun "if", on a forcément (face, sens, double) de rempli


# permet la saisie d'une suite de mouvements à effectuer		
# renvoie toujours une liste de tuples valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvements():      # on demande à l'utilisateur de donner une suite de mouvements sans espace en majuscules et dans le bon odre
     # on crée une liste qui va recevoir dans un premier temps les chaines de caractère des mouvements isolés, puis des tuples valides
     l=[]
     c="" # variable provisoire recevant la chaine de caractère de chaque moyvement isolé
     inser=input("Donner une suite de mouvements valides: ")
     if len(inser)==1:
          # on vérifie dans ce cas que l'utilisateur a bien rentré une face
          if inser[0] in FA:
               l.append(inser[0])
               return [(l[0],True,False)]
          else:
               # sinon il doit recommencer depuis le début
               return saisie_mouvements()
     if len(inser)==2:
          # on vérifie que l'utilisateur a bien renseigné une face en premier
          if inser[0] in FA:
               # puis un sens
               if inser[1]=="'":
                    l.append(inser[0]+inser[1]) 
               # ou un double  
               if inser[1]=="2":
                    l.append(inser[0]+inser[1])
               # ou un deuxième mouvement de face
               if inser[1] in FA:
                    l.append(inser[0])
                    l.append(inser[1])
               # sinon, il a fait une erreur et doit recommencer
               elif inser[1]!="'" and inser[1]!="2" and inser[1] not in FA:
                    return saisie_mouvements()
          # idem si la première face contient une erreur
          elif inser[0] not in FA:
               return saisie_mouvements()
     # si la saisie de mouvement contient plus de 2 termes, alors il y a une condition d'arret à respecter
     i=0 # parcourt la chaine de caractère saisie par l'utilisateur
     while i<len(inser)-2: # on s'arrête deux termes avant la fin de la saisie
          # on cherche à parcourir la liste afin d'isoler les chaines de caractère de chaque mouvement
          # on verifie que l'utilisateur ait bien rentré face, face-sens, face-double, face-sens-double
          if inser[i] in FA: 
               if inser[i+1]=="'":
                    if inser[i+2]=="2":
                         c=inser[i:i+3]
                         l.append(c) # on ajoute le mouvement à la liste
                    else:
                         c=inser[i:i+2]
                         l.append(c)
               elif inser[i+1]=="2":
                    if inser[i+2]=="'":
                         return saisie_mouvements()
                    else:
                         c=inser[i:i+2]
                         l.append(c)
               elif inser[i+1]!="'" and inser[i+1]!="2":
                    c=inser[i]
                    l.append(c)
          if inser[i] not in FA:
               return saisie_mouvements()
          i+=len(c)  # len(c) désigne la longueur du mouvement élémentaire isolé et le compteur de la boucle i est incrémenté de façon à ce que inser[i] soit toujours, si la saisie est correcte, une face
     r=len(inser)-i # c'est ce qui reste à parcourir de la saisie utilisateur
     if r==0: # s'il ne reste rien à parcourir, la saisie est vide, ou le travail s'est terminé dans la boucle while
          if l==[]:
               return saisie_mouvements()
     if r==1:
          if inser[len(inser)-1] in FA:
               l.append(inser[len(inser)-1])
          else:
               return saisie_mouvements()
     if r==2 and i!=0:   # s'il reste 2 éléments dans la chaine de caractère, mais que l'on a parcouru la boucle (conflit avec le deuxieme "if" de la fonction)       
          if inser[len(inser)-2] in FA: # on procède de la même façon en vérifiant face-face, face-sens, face-double
               if inser[len(inser)-1]=="'" or inser[len(inser)-1]=="2":
                    l.append(inser[len(inser)-2]+inser[len(inser)-1])
               if inser[len(inser)-1] in FA:
                    l.append(inser[len(inser)-2])
                    l.append(inser[len(inser)-1])
               if inser[len(inser)-1]!="'" and inser[len(inser)-1]!="2" and inser[len(inser)-1] not in FA:
                    return saisie_mouvements()
          if inser[len(inser)-2] not in FA:
               return saisie_mouvements()
     # la liste l contient maintenant uniquement des chaines de caractères de mouvement isolés et vaildes, il suffit de les décomposer en tuples (face,sens,double)
     for k in range (len(l)):
          if len(l[k])==1: # c'est forcément une face
               l[k]=(l[k][0],True,False)
          elif len(l[k])==2 and l[k][1]=="'": # cas face-sens
               l[k]=(l[k][0],False,False)
          elif len(l[k])==2 and l[k][1]=="2": # cas face-double
               l[k]=(l[k][0],True,True)
          elif len(l[k])==3: # cas face-sens-double
               l[k]=(l[k][0],False,True)
     return l
     # on retourne le mouvement valide sous forme de liste de tuples de mouvements élémentaires sous forme (face, sens, double)