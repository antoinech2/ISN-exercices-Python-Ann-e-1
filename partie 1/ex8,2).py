#Python - Exercice 8, 2)
#Script qui détermine si une chaine de caractère donnée est un palindrome,
#ou donne l'entrée avec les caractères inversés si ce n'est pas le cas.

#Lecture de l'entrée
phrase=input("Entrez une phrase ou un mot:")

#Initialisation des variables
longeur=len(phrase)
boucle=longeur-1
char_inverse=""

#Boucle du nombre de caractères de l'entrée
while(boucle>=0):
    #On ajoute le caractère a la variable du texte inversé; en partant de la fin du texte
    char_inverse=char_inverse+phrase[boucle]
    boucle-=1

#Si le texte d'origine est identique au texte inversé:
if phrase == char_inverse:
    #On affiche que c'est un palindrome
    print("Votre phrase/mot est un palindrome! Voici votre phrase/mot inversé(e):",char_inverse)
else:
    #Sinon on affiche le texte inversé
    print("Votre n'est pas un palindrome; Voici votre phrase/mot inversé(e):",char_inverse)
