#Programme qui affiche des "*", avec une "*" de plus a chaque ligne, 7 fois.

a=1
b="*"
while a<=7 : # boucle 7 fois
    print(b)
    b=b+"*"  #Ajout d'un "*" a la précédente variable
    a=a+1
