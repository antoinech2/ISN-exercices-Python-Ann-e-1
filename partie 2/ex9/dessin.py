#Python - Partie 2 - Exercice 9
#Script qui affiche 8 carré à la suite.

#Importation des module
from turtle import *
from dessins_tortue import *

#Lecture de l'entrée
taille=int(input("Entrez la taille des carrés."))
couleur=input("Entrez la couleur des carrés. (en anglais)")

for i in range (8):
    down()
    carre(taille,couleur)
    up()
    goto (xcor()+taille+20,ycor())
    
