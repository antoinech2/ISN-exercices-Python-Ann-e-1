note=float(input("Entrez votre note sur 20:"))
if note>=0 or note<=20:
    print("Note invalide. Entrez un nombre compris entre 0 et 20")
elif note == 0:
    print("C'est lamentable!")
elif note<10:
    print("C'est en dessous de la moyenne.")
elif note<20:
    print("J'ai la moyenne!")
elif note == 20:
    print("C'est excellent!")
