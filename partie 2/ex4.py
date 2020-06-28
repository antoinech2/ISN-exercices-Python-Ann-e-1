#Python - Partie 2- Exercice 3
#Script qui affiche un dessin d'un vélo et un arbre.

#Importation du module
from turtle import *

#Définition de la fonction "hexa":
def DrawHexa(couleur, centerx, centery, long, coord_relatif=False, angle_relatif=False, angle=0):
    up()
    if angle_relatif:
        right(angle)
    else:
        setheading(angle)
    if coord_relatif:
        goto(xcor()+centerx,ycor()+centery)
    else:
        goto(centerx,centery)
    color(couleur)
    down()
    for a in range (6):
        for i in range (3):
            forward(long)
            right(120)
        left(60)
    up()


mode('logo')
width(3)
speed('fastest')
title('Mon dessin')



#Sol:
setheading(90)
color('gray')
goto(-200,0)
down()
forward(400)
up()

#Arbre
#Tronc
color('brown')
goto(120,0)
left(90)
down()
forward(170)
up()

#Feuille haut
DrawHexa('darkgreen', 120, 220, 50, False, False, 0)

#Branche/Feuille côté bas
color('brown')
goto(120,75)
left(75)
down()
forward(30)
up()
forward(30)
DrawHexa('darkgreen', 0, 0, 30, True, True, 0)


#Branche/Feuille côté haut
color('brown')
goto(120,140)
#left(75)
down()
forward(30)
up()
forward(30)
DrawHexa('darkgreen', 0, 0, 30, True, True, 0)

#Vélo roue droite
DrawHexa('yellow', 0, 30, 30, False, False, 0)

#Vélo roue gauche
DrawHexa('yellow', -136, 30, 30, False, False, 0)


#Vélo
color('orange')
goto(0,30)
down()
setheading(270)
for i in range (4):
    forward(68)
    right(120)
up()

left(60)
down()
for i in range (3):
    forward(68)
    right(120)
    
up()

goto(-136,30)
down()
setheading(30)
forward(68)
right(120)
up()

goto(-102,89)
down()
setheading(50)
color('red')
forward(30)
up()

goto(-34,89)
down()
setheading(45)
forward(30)
setheading(270)
forward(25)

#Nuages
DrawHexa('lightblue', -30, 220, 15, False, False, 0)
DrawHexa('lightblue', -55, 180, 15, False, False, 0)
DrawHexa('lightblue', -100, 220, 15, False, False, 0)
DrawHexa('lightblue', -125, 180, 15, False, False, 0)
DrawHexa('lightblue', -170, 215, 15, False, False, 0)

hideturtle()
