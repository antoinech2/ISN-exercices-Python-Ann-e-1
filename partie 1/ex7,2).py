#Python - Exercice 7, 2)
#Script qui détermine le nombre de lettres "e" dans une phrase/mot donnée.

#Lecture de l'entrée
phrase=input("Entrez une phrase ou un mot.")

#Initialisation des variables
longeur=len(phrase)
boucle=0
compteur=0

#Boucle du nombre de caractères de l'entrée
while(boucle<longeur):
    #Si le caractère est un "e"
    if phrase[boucle] == "e":
        #On ajoute 1 au compteur de "e"
        compteur+=1
    boucle+=1
#Si il y a au moins un "e":
if compteur>0:
    #On affiche le nombre de "e"
    print('La chaîne de caractère contient la lettre "e"',compteur,"fois")
else:
    #Sinon on affiche qu'il n'y a pas de "e"
    print('La chaîne de caractère ne contient pas la lettre "e"')
