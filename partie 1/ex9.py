#Python - Exercice 9
#Script qui affiche le nom des mois avec leur nombre de jours.

#Initialisation des variables/listes
boucle=0

#Liste des jours dans chaque mois
jours=[31,28,31,30,31,30,31,31,30,31,30,31]

#Liste des noms des mois
mois=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

#Troisième liste qui va contenir les éléments des deux premières
nbjour=[0]

#Boucle 12 fois pour chaque éléments des listes "jours" et "mois".
while boucle<12: 
    nbjour.append(mois[boucle])
    nbjour.append(jours[boucle])
    boucle+=1

#Réinitialisation de la variable de la boucle
boucle=0

#Boucle 12 fois pour afficher les mois et les jours.
while boucle<12:
    print(nbjour[boucle*2+1],":",nbjour[boucle*2+2])
    boucle+=1
