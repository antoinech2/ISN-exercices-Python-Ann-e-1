#Python - Partie 2 - Exercice 9
#Script qui affiche 8 carré à la suite.

#Importation des module
from turtle import *
from dessins_tortue import *

#Lecture de l'entrée
taille_carre=int(input("Entrez la taille de départ des carrés."))
taille_triangle=int(input("Entrez la taille de départ des triangles."))
couleur_carre=input("Entrez la couleur de départ des carrés.")
couleur_triangle=input("Entrez la couleur de départ des triangles.")

#Tailles:
#Carré: 30
#Triangle: 27

up()
goto(-300,0)

for i in range (5):
    down()
    carre(taille_carre,couleur_carre,0)
    up()
    goto (xcor()+taille_carre+10,ycor())
    down()
    triangle(taille_triangle,couleur_triangle,0)
    up()
    goto (xcor()+taille_triangle+10,ycor())
    taille_carre += 10
    taille_triangle += 10
