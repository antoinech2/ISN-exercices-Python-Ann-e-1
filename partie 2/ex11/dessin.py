#Python - Partie 2 - Exercice 9
#Script qui affiche 8 carré à la suite.

#Importation des module
from turtle import *
from dessins_tortue import *

#Lecture de l'entrée
taille=int(input("Entrez la taille de départ des étoiles."))
couleur=input("Entrez la couleur de départ des étoiles.")

#Tailles:
#Carré: 30
#Triangle: 27


up()
goto(-300,0)

for i in range (9):
    down()
    etoile5(taille,couleur,0)
    up()
    goto(xcor()+taille+10,ycor())
    if i <= 3:
        taille += 15
    else:
        taille -= 15
