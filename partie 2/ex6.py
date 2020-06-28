#Python - Partie 2- Exercice 6
#Script qui affiche des triangles de couleurs différentes a différents endroits.

#Importation des module
from turtle import *
from random import *

speed("fastest")

def DrawTriangle(couleur_r,couleur_g,couleur_b):
    up()
    goto(randint(-400,400),randint(-400,400))
    setheading(randint(0,359))
    color((couleur_r,couleur_g,couleur_b))
    down()
    for i in range (3):
        forward(110)
        right(120)
    up()

colormode(255)
width(2)

while 1:
    DrawTriangle(randint(0,255),randint(0,255),randint(0,255))
