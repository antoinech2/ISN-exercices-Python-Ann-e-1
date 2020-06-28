#Python - Partie 2- Exercice 6
#Script qui affiche des triangles de couleurs différentes a différents endroits.

#Importation des module
from turtle import *
from random import *

def DrawTriangle(taille,pos_x,pos_y):
    up()
    goto(pos_x,pos_y)
    setheading(0)
    color(randint(0,255),randint(0,255),randint(0,255))
    down()
    for i in range (3):
        forward(taille)
        right(120)
    up()

colormode(255)
width(2)

DrawTriangle(189,-150,65)
