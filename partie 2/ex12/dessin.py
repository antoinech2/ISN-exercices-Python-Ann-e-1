#Python - Partie 2 - Exercice 9
#Script qui affiche 8 carré à la suite.

#Importation des module
from turtle import *
from dessins_tortue import *

#Tailles:
#Carré: 30
#Triangle: 27


up()
goto(-80,240)
angle=0
taille = 60
speed("fast")

down()
carre(taille,"blue",angle)
up()
goto(0,280)

for i in range (9):
    angle-=60
    taille-=5
    up()
    setheading(angle)
    forward(taille)
    down()
    etoile6(taille,"red",angle)
    up()
    setheading(angle)
    forward(taille)
    down()
    triangle(taille,"green",angle)
    up()
    forward(taille+20)
    down()
    etoile5(taille,"brown",angle)
    up()
    forward(taille+20)
    down()
    carre(taille,"blue",angle)
    up()
    setheading(angle+20)
    forward(taille+30)
    up()
