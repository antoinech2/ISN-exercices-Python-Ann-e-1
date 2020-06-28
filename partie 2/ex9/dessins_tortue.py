#Python - Partie 2 - Exercice 9
#Script qui définit les fonctions pour un autre script.

#Importation des module
from turtle import *

def carre(taille, couleur):
    color(couleur)
    for i in range (4):
        forward(taille)
        right(90)
