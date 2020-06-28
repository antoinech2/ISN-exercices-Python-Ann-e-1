chaine=input("Entrez une phrase ou un mot.")
long=len(chaine)
a=long-1
char_inverse=""
while(a>=0):
    char_inverse=char_inverse+chaine[a]
    a=a-1
print("Voici votre phrase/mot inversé(e):",char_inverse)
