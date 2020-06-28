#Python - Partie 2 - Exercice 9
#Script qui définit les fonctions pour un autre script.

#Importation des module
from turtle import *
from math import *

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

def triangleleft(taille, couleur, angle):
    setheading(angle)
    color(couleur)
    for i in range (3):
        forward(taille)
        left(120)

def etoile5(taille, couleur, angle):
    setheading(angle)
    color(couleur)
    for i in range (5):
        forward(taille)
        right(144)

def etoile6(taille, couleur, angle):
    color(couleur)
    down()
    triangle(taille, couleur, angle)
    up()
    right(30)
    forward(taille/sqrt(3))
    left(120)
    forward(taille/sqrt(3))
    down()
    triangleleft(taille, couleur, heading()+150)
