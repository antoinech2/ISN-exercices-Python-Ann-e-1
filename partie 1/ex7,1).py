chaine=input("Entrez une phrase ou un mot.")
long=len(chaine)
a=0
result=False
while(a<long):
    if chaine[a]=="e":
        result=True
    a=a+1
if result==True:
    print('La chaine de caractère contient la lettre "e"')
else:
    print('La chaine de caractère ne contient pas la lettre "e"')
