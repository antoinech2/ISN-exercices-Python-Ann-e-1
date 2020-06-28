#Python - Partie 2 - Exercice 9
#Script qui définit les fonctions pour un autre script.

#Importation des module
from turtle import *

def carre(taille, couleur, angle):
    setheading(angle)
    color(couleur)
    for i in range (4):
        forward(taille)
        right(90)

def triangle(taille, couleur, angle):
    setheading(angle)
    color(couleur)
    for i in range (3):
        forward(taille)
        right(120)

def etoile5(taille, couleur, angle):
    setheading(angle)
    color(couleur)
    for i in range (5):
        forward(taille)
        right(144)
