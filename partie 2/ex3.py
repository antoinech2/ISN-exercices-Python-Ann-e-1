#Python - Partie 2- Exercice 3
#Script qui affiche un carré de 100p de côté, de contour vert et de fond rouge

#Importation du module
from turtle import *

#Initialisation des variables/listes
cote = 100

color('green')
goto(0,0)
down()
fillcolor('red')
begin_fill()
#Boucle 4 fois pour chaque coté du carré
for a in range (4):
    forward(cote)
    right(90)
end_fill()
up()
