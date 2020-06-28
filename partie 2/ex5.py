#Python - Partie 2 - Exercice 5
#Script qui détermine si une année est bissextile ou non.

#Lecture de l'entrée
annee=int(input('Entrez une année.'))


if annee%4:
    if not annee%100 and annee%400:
        bissextile==True
    else:
        bissextile=False  
else:
    bissextile=False



if bissextile==True:
    print("L'année",annee,"est une année bissextile")
else:
    print("L'année",annee,"n'est pas une année bissextile")
